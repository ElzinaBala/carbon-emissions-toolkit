import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output, State, dash_table
import pandas as pd
import io
import base64
import plotly.express as px

from src.carbon_calculator import CarbonCalculator
from src.emissions_analysis import EmissionsAnalysis

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Carbon Emissions Dashboard"

app.layout = dbc.Container([
    html.H1("Carbon Emissions Toolkit", className="my-3"),
    dcc.Upload(
        id='upload-data',
        children=html.Div([
            "Drag and drop or ",
            html.A("select a CSV file")
        ]),
        style={
            'width': '100%',
            'padding': '30px',
            'borderWidth': '2px',
            'borderStyle': 'dashed',
            'textAlign': 'center',
        },
        multiple=False
    ),
    html.Div(id='summary'),
    html.Hr(),
    html.Div(id='hotspots'),
    html.Hr(),
    dbc.Row([
        dbc.Col([
            html.Label("Select activity type:"),
            dcc.Dropdown(id='activity-type-dropdown')
        ]),
        dbc.Col([
            html.Label("Reduction %:"),
            dcc.Slider(0, 100, 5, value=20, id='reduction-slider')
        ]),
    ]),
    html.Div(id='reduction-output'),
    html.Br(),
    html.A("Download Adjusted Data", id="download-link", download="adjusted_emissions.csv", href="", target="_blank")
], fluid=True)

def parse_contents(contents, filename):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
    return df

@app.callback(
    [Output('summary', 'children'),
     Output('hotspots', 'children'),
     Output('activity-type-dropdown', 'options'),
     Output('download-link', 'href'),
     Output('reduction-output', 'children')],
    [Input('upload-data', 'contents'),
     Input('activity-type-dropdown', 'value'),
     Input('reduction-slider', 'value')],
    [State('upload-data', 'filename')]
)
def update_output(contents, activity_type, reduction_percent, filename):
    if contents is None:
        return "", "", [], "", ""

    df = parse_contents(contents, filename)

    if 'Quantity' not in df.columns or 'Emission_Factor' not in df.columns:
        return html.Div("Missing required columns: 'Quantity' and 'Emission_Factor'."), "", [], "", ""

    # Calculate emissions
    calculator = CarbonCalculator(df)
    emissions_df = calculator.calculate_emissions()
    total_emissions = emissions_df['Emissions_CO2e_kg'].sum()

    # Summary Table
    summary_table = emissions_df.groupby("Activity_Type")["Emissions_CO2e_kg"].sum().reset_index()

    # Bar Chart
    bar_fig = px.bar(
        summary_table.sort_values(by="Emissions_CO2e_kg", ascending=False),
        x="Activity_Type",
        y="Emissions_CO2e_kg",
        title="Emissions by Activity Type (Bar Chart)",
        labels={"Emissions_CO2e_kg": "kg CO₂e"},
        text_auto=".2s"
    )

    # Pie Chart
    pie_fig = px.pie(
        summary_table,
        names="Activity_Type",
        values="Emissions_CO2e_kg",
        title="Emissions Distribution by Activity (Pie Chart)"
    )

    # Time Series (if 'Date' column exists)
    if 'Date' in emissions_df.columns:
        try:
            emissions_df['Date'] = pd.to_datetime(emissions_df['Date'], errors='coerce')
            trend_df = emissions_df.groupby('Date')["Emissions_CO2e_kg"].sum().reset_index()
            trend_fig = px.line(
                trend_df,
                x='Date',
                y='Emissions_CO2e_kg',
                title="Emissions Over Time (Line Chart)",
                markers=True,
                labels={"Emissions_CO2e_kg": "kg CO₂e"}
            )
            trend_chart = dcc.Graph(figure=trend_fig)
        except Exception:
            trend_chart = html.Div("Invalid dates in 'Date' column. Cannot display time series.")
    else:
        trend_chart = html.Div("No 'Date' column found — add one to enable time trend visualization.")

    # Full summary layout
    summary_layout = html.Div([
        html.H4("Total Emissions: {:.2f} kg CO₂e".format(total_emissions)),
        dash_table.DataTable(
            summary_table.to_dict("records"),
            [{"name": i, "id": i} for i in summary_table.columns],
            style_table={"overflowX": "auto"},
            page_size=10
        ),
        html.Br(),
        dcc.Graph(figure=bar_fig),
        html.Br(),
        dcc.Graph(figure=pie_fig),
        html.Br(),
        trend_chart
    ])

    # Hotspots
    analysis = EmissionsAnalysis(emissions_df)
    hotspots_df = analysis.identify_hotspots(5)

    hotspots_layout = html.Div([
        html.H5("Top 5 Emission Records"),
        dash_table.DataTable(
            hotspots_df[['Record_ID', 'Activity_Type', 'Quantity', 'Emission_Factor', 'Emissions_CO2e_kg']].to_dict("records"),
            [{"name": i, "id": i} for i in hotspots_df.columns],
            page_size=5
        )
    ])

    options = [{"label": i, "value": i} for i in emissions_df['Activity_Type'].unique()]

    # Simulate reduction
    if activity_type:
        reduced_df = analysis.simulate_reduction(activity_type, reduction_percent)
        new_total = reduced_df['Emissions_CO2e_kg'].sum()

        download_csv = reduced_df.to_csv(index=False)
        download_href = "data:text/csv;charset=utf-8," + base64.b64encode(download_csv.encode()).decode()

        reduction_layout = html.Div([
            html.H6(f"New Total After {reduction_percent}% Reduction in {activity_type}: {new_total:.2f} kg CO₂e")
        ])
    else:
        download_href = ""
        reduction_layout = ""

    return summary_layout, hotspots_layout, options, download_href, reduction_layout

if __name__ == '__main__':
    app.run(debug=True)

import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px
import os

# Load default emissions dataset
data_path = os.path.join("data", "raw", "emissions_data.csv")
df = pd.read_csv(data_path)

# Preprocess
df["Date"] = pd.to_datetime(df["Date"])
df["Emissions_CO2e_kg"] = df["Quantity"] * df["Emission_Factor"]

# Create figures
bar_chart = px.bar(
    df,
    x="Activity_Type",
    y="Emissions_CO2e_kg",
    color="Activity_Type",
    title="Emissions by Activity Type",
    template="plotly",
    labels={"Emissions_CO2e_kg": "Emissions (kg CO2e)"},
    text_auto=".2s"
)

pie_chart = px.pie(
    df,
    names="Sector_Code",
    values="Emissions_CO2e_kg",
    title="Emissions Share by UNFCCC Tier 1 Sector",
    color_discrete_sequence=px.colors.qualitative.Set3
)

line_chart = px.line(
    df.sort_values("Date"),
    x="Date",
    y="Emissions_CO2e_kg",
    color="Activity_Type",
    title="Emissions Trend Over Time",
    template="plotly_dark",
    markers=True
)

stacked_bar_chart = px.bar(
    df,
    x="Sector_Name",
    y="Emissions_CO2e_kg",
    color="Activity_Type",
    title="Emissions by Sector and Activity",
    barmode="stack",
    template="plotly_white"
)

sunburst_chart = px.sunburst(
    df,
    path=["Sector_Name", "Activity_Type"],
    values="Emissions_CO2e_kg",
    title="Emissions Breakdown by Sector and Activity",
    color="Emissions_CO2e_kg",
    color_continuous_scale="RdBu"
)

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("Carbon Emissions Dashboard", style={"textAlign": "center"}),

    html.Div([
        dcc.Graph(figure=bar_chart),
        dcc.Graph(figure=pie_chart),
        dcc.Graph(figure=line_chart),
        dcc.Graph(figure=stacked_bar_chart),
        dcc.Graph(figure=sunburst_chart),
    ], style={"maxWidth": "1000px", "margin": "auto"})
])

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=8050)

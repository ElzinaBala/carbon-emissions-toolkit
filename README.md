# Carbon Emissions Toolkit

A professional, interactive greenhouse gas (GHG) accounting and analysis dashboard built using Dash. This toolkit enables transparent, data-driven carbon emissions analysis, reduction scenario modeling, and visual reporting to support sustainability initiatives and climate compliance strategies.

## Project Purpose

As climate policies tighten and sustainability becomes a strategic priority, organizations must accurately monitor, analyze, and reduce their carbon footprints. This toolkit is designed to replicate the core responsibilities of a Carbon and Emissions Analyst, enabling:

- GHG data ingestion, validation, and carbon footprint calculation
- Identification of emissions hotspots
- Interactive scenario modeling for emissions reduction
- Dynamic visual analytics (bar, pie, time series)
- Downloadable adjusted datasets

It is aligned with standard carbon accounting practices such as the GHG Protocol, IPCC Tier 1 methods, and Scope 1–3 boundaries.


## Features

| Module                     | Description |
|---------------------------|-------------|
| CSV Upload                | Upload GHG activity data in a standard tabular format |
| Carbon Calculator         | Computes emissions in kilograms CO2e using activity data times emission factors |
| Hotspot Identifier        | Flags the most emission-intensive activities or records |
| Scenario Modeler          | Simulates CO2e reductions for any activity type and percentage |
| Data Visualizations       | Bar, pie, and line charts for emission insights |
| Download Tool             | Export adjusted emissions dataset for reporting |

## Dashboard Visualizations

- Bar Chart: Emissions by activity type
- Pie Chart: Share of total emissions per activity
- Time Series: Emissions trend over time (if Date column is provided)

## Sample Input Format

Your CSV file should have at minimum the following columns:

| Record_ID | Activity_Type | Quantity | Emission_Factor | Unit       | Date (optional) |
|-----------|----------------|----------|------------------|------------|-----------------|
| 1         | Electricity     | 500      | 0.233            | kWh        | 2023-01-01      |
| 2         | Travel          | 300      | 2.31             | km         | 2023-01-03      |

Emissions are calculated as:

`Emissions_CO2e_kg = Quantity × Emission_Factor`

## Deployment (via Render)

This app is deployed using Render.

## Live Dashboard

A fully interactive version of this carbon emissions analysis dashboard is deployed on Render and accessible at:

[https://carbon-emissions-toolkit.onrender.com](https://carbon-emissions-toolkit.onrender.com)

This hosted application showcases a realistic GHG inventory reporting toolkit, aligned with UNFCCC Tier 1 sector codes and activity-based carbon calculations. It features dynamic, professional visualizations including:

- Emissions by activity type and sector
- Pie chart illustrating emissions share by UNFCCC categories
- Time series of emissions trends over time
- Sectoral emissions breakdown with stacked bar and sunburst charts

This project is ideal for demonstrating expertise in carbon accounting, sustainability reporting, and MRV (Monitoring, Reporting, Verification) frameworks supporting climate action.

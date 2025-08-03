# Carbon Emissions Analysis Toolkit

This project provides a professional dashboard for analyzing greenhouse gas (GHG) emissions using activity-based data and UNFCCC Tier 1 sector classifications. It includes data processing logic, emission calculations, and a fully interactive Dash web application. The toolkit is suitable for use in sustainability reporting, climate action tracking, and MRV (Measurement, Reporting, and Verification) systems.

---

## Features

- Structured input format for activity-level emissions data
- Support for UNFCCC Tier 1 sector codes (e.g., 1A1, 3B, 5D)
- Emissions calculation using standard emission factors
- Auto-generated visualizations:
  - Bar chart by activity type
  - Pie chart by UNFCCC sector
  - Time series emissions trend
  - Stacked bar by sector and activity
  - Sunburst chart for hierarchical sector analysis
- Clean, modern UI built with Plotly Dash
- Live-hosted demo (see below)

---

## Live Demo

A live, fully interactive version of this carbon emissions dashboard is available online:

[https://carbon-emissions-toolkit.onrender.com](https://carbon-emissions-toolkit.onrender.com)

The dashboard presents greenhouse gas emissions data following UNFCCC Tier 1 sector classifications. It provides comprehensive visualizations, including emissions by activity type, sector shares, temporal trends, and hierarchical breakdowns.

This live demo highlights the practical application of carbon accounting and sustainability reporting techniques, suitable for climate action and MRV initiatives.

---

## Project Structure

```
carbon-emissions-toolkit/
├── dashboard/
│   └── app.py                  # Dash app entry point
├── data/
│   └── raw/
│       └── emissions_data.csv  # Default input data file
├── requirements.txt           # Dependencies for the app
├── render.yaml                # Deployment config for Render
├── README.md                  # Project documentation
└── generate_data.py           # Script to create example dataset
```

---

## Getting Started Locally

### 1. Clone the repository

```bash
git clone https://github.com/ElzinaBala/carbon-emissions-toolkit.git
cd carbon-emissions-toolkit
```

### 2. Create virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the app

```bash
python dashboard/app.py
```

Then open your browser at `http://localhost:8050`

---

## Deployment (Render)

This app is deployed using [Render](https://render.com), a cloud platform for static and dynamic web applications.

### render.yaml

```yaml
services:
  - type: web
    name: carbon-emissions-toolkit
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: python dashboard/app.py
    plan: free
```

Push your repo to GitHub and connect it to a new Render web service. The app will be built and deployed automatically.

---

## Example Dataset

An example dataset is included under `data/raw/emissions_data.csv` and contains sample records structured like this:

```csv
Record_ID,Sector_Code,Sector_Name,Activity_Type,Quantity,Emission_Factor,Unit,Date
1,1A1,Energy industries,Electricity,500,0.233,kWh,2023-01-01
2,1A3,Transport,Road Travel,300,2.31,km,2023-01-03
3,2C,Industrial processes,Cement Production,150,0.92,tonnes,2023-01-04
4,3B,Agriculture,Crop Burning,200,1.7,hectares,2023-01-06
5,5D,Waste,Wastewater Handling,1000,0.85,m3,2023-01-08
```

---

## License

This project is open-source and freely available for academic, professional, and educational use.


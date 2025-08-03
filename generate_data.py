import pandas as pd
import os

# Define dataset
data = {
    "Record_ID": [1, 2, 3, 4, 5],
    "Sector_Code": ["1A1", "1A3", "2C", "3B", "5D"],
    "Sector_Name": [
        "Energy industries",
        "Transport",
        "Industrial processes",
        "Agriculture",
        "Waste"
    ],
    "Activity_Type": [
        "Electricity",
        "Road Travel",
        "Cement Production",
        "Crop Burning",
        "Wastewater Handling"
    ],
    "Quantity": [500, 300, 150, 200, 1000],
    "Emission_Factor": [0.233, 2.31, 0.92, 1.7, 0.85],
    "Unit": ["kWh", "km", "tonnes", "hectares", "m3"],
    "Date": [
        "2023-01-01",
        "2023-01-03",
        "2023-01-04",
        "2023-01-06",
        "2023-01-08"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Ensure folder exists
output_path = os.path.join("data", "raw")
os.makedirs(output_path, exist_ok=True)

# Save to CSV
df.to_csv(os.path.join(output_path, "emissions_data.csv"), index=False)

print("CSV file generated at data/raw/emissions_data.csv")

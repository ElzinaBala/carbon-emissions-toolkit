import pandas as pd
import os

class ReportGenerator:
    """
    Generates emissions summary reports as Excel files.
    """

    def __init__(self, data, output_path="reports/emissions_summary.xlsx"):
        self.data = data
        self.output_path = output_path
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

    def generate_summary_report(self):
        """
        Creates an Excel report with:
        - Summary of total emissions
        - Top 5 emission sources
        """
        with pd.ExcelWriter(self.output_path, engine="openpyxl") as writer:
            # Write full dataset
            self.data.to_excel(writer, sheet_name="All Data", index=False)

            # Emissions summary by Activity_Type
            summary = self.data.groupby("Activity_Type")["Emissions_CO2e_kg"].sum().reset_index()
            summary = summary.sort_values(by="Emissions_CO2e_kg", ascending=False)
            summary.to_excel(writer, sheet_name="Summary by Activity", index=False)

            # Top 5 emission sources
            top5 = self.data.sort_values(by="Emissions_CO2e_kg", ascending=False).head(5)
            top5.to_excel(writer, sheet_name="Top 5 Records", index=False)

        print(f"Report generated: {self.output_path}")


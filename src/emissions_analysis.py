import pandas as pd

class EmissionsAnalysis:
    """
    Analyzes emissions data to identify hotspots and simulate reduction scenarios.
    """

    def __init__(self, data):
        """
        :param data: DataFrame with emissions calculated (must include 'Emissions_CO2e_kg').
        """
        self.data = data

    def identify_hotspots(self, top_n=5):
        """
        Identifies the top N emission sources by Emissions_CO2e_kg.
        """
        hotspots = self.data.sort_values(by='Emissions_CO2e_kg', ascending=False).head(top_n)
        return hotspots

    def simulate_reduction(self, activity_type, reduction_percent):
        """
        Simulates emission reductions by decreasing the emission factor or quantity.
        
        :param activity_type: Type of activity to apply reduction (e.g. 'Diesel').
        :param reduction_percent: Percent reduction (0-100).
        :return: DataFrame with adjusted emissions.
        """
        modified_data = self.data.copy()

        mask = modified_data['Activity_Type'] == activity_type
        if mask.sum() == 0:
            print(f"No activity found for: {activity_type}")
            return modified_data

        # Apply reduction
        modified_data.loc[mask, 'Emission_Factor'] *= (1 - reduction_percent / 100)
        modified_data['Emissions_CO2e_kg'] = modified_data['Quantity'] * modified_data['Emission_Factor']

        return modified_data

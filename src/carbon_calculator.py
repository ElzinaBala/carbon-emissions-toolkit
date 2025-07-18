import pandas as pd

class CarbonCalculator:
    """
    A class to calculate CO2e emissions based on activity data and emission factors.
    """

    def __init__(self, data):
        """
        Initializes the calculator with a pandas DataFrame.
        :param data: DataFrame with 'Quantity' and 'Emission_Factor' columns.
        """
        self.data = data.copy()

    def calculate_emissions(self):
        """
        Calculates total emissions (CO2e) for each record.
        Adds a new 'Emissions_CO2e_kg' column to the dataframe.
        """
        if 'Quantity' not in self.data.columns or 'Emission_Factor' not in self.data.columns:
            raise ValueError("Data must include 'Quantity' and 'Emission_Factor' columns.")

        self.data['Emissions_CO2e_kg'] = self.data['Quantity'] * self.data['Emission_Factor']
        return self.data

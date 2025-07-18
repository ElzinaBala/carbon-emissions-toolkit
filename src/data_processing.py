import pandas as pd

class DataProcessor:
    """
    A class to handle data ingestion, validation, and cleaning for GHG emissions analysis.
    """

    REQUIRED_COLUMNS = [
        'Record_ID', 
        'Source_Category', 
        'Activity_Type', 
        'Unit', 
        'Quantity', 
        'Emission_Factor', 
        'Emission_Factor_Unit', 
        'Period'
    ]

    def __init__(self, filepath):
        """
        Initializes the DataProcessor with the data file path.
        """
        self.filepath = filepath
        self.data = None

    def load_data(self):
        """
        Loads data from CSV or Excel into a pandas DataFrame.
        """
        if self.filepath.endswith('.csv'):
            self.data = pd.read_csv(self.filepath)
        elif self.filepath.endswith(('.xls', '.xlsx')):
            self.data = pd.read_excel(self.filepath)
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")
        print("Data loaded successfully.")
        return self.data

    def validate_data(self):
        """
        Validates that all required columns are present and checks for missing values.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Run load_data() first.")
        
        missing_columns = [col for col in self.REQUIRED_COLUMNS if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
        
        if self.data.isnull().any().any():
            missing_data = self.data.isnull().sum()
            print("Warning: Missing values detected:\n", missing_data)
        else:
            print("No missing values detected.")

    def clean_data(self):
        """
        Performs data cleaning operations like trimming whitespace and standardizing units.
        """
        if self.data is None:
            raise ValueError("Data not loaded. Run load_data() first.")

        self.data = self.data.applymap(lambda x: x.strip() if isinstance(x, str) else x)
        print("Data cleaned: whitespaces removed.")
        return self.data


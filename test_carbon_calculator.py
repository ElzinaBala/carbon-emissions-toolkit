from src.data_processing import DataProcessor
from src.carbon_calculator import CarbonCalculator

if __name__ == "__main__":
    processor = DataProcessor('data/raw/emissions_data.csv')
    df = processor.load_data()
    processor.validate_data()
    cleaned = processor.clean_data()

    calculator = CarbonCalculator(cleaned)
    result = calculator.calculate_emissions()

    print(result[['Record_ID', 'Quantity', 'Emission_Factor', 'Emissions_CO2e_kg']])

from src.data_processing import DataProcessor
from src.carbon_calculator import CarbonCalculator
from src.emissions_analysis import EmissionsAnalysis

if __name__ == "__main__":
    processor = DataProcessor('data/raw/emissions_data.csv')
    df = processor.load_data()
    processor.validate_data()
    cleaned_data = processor.clean_data()

    calculator = CarbonCalculator(cleaned_data)
    emissions_data = calculator.calculate_emissions()

    analysis = EmissionsAnalysis(emissions_data)

    print("=== Top Emission Hotspots ===")
    print(analysis.identify_hotspots(top_n=3))

    print("\n=== Simulating 20% Reduction in Diesel Emissions ===")
    reduced_data = analysis.simulate_reduction('Diesel', 20)
    print(reduced_data[['Record_ID', 'Activity_Type', 'Quantity', 'Emission_Factor', 'Emissions_CO2e_kg']])

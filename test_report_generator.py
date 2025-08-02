from src.data_processing import DataProcessor
from src.carbon_calculator import CarbonCalculator
from src.report_generator import ReportGenerator

if __name__ == "__main__":
    processor = DataProcessor('data/raw/emissions_data.csv')
    df = processor.load_data()
    processor.validate_data()
    cleaned = processor.clean_data()

    calculator = CarbonCalculator(cleaned)
    emissions_df = calculator.calculate_emissions()

    report = ReportGenerator(emissions_df)
    report.generate_summary_report()

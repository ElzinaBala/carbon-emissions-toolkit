from src.data_processing import DataProcessor

if __name__ == "__main__":
    processor = DataProcessor('data/raw/emissions_data.csv')
    df = processor.load_data()
    processor.validate_data()
    cleaned_data = processor.clean_data()
    print(cleaned_data)

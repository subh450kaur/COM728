# Loading data using CSV module
import pandas as pd


def load_data(file):
    try:
        data = []
        with open(file, 'r') as file:
            headers = file.readline().strip().split(',')
            for line in file:
                row = line.strip().split(',')
                data.append(dict(zip(headers, row)))
        return data
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return []


# Loading data using Pandas module
def load_data_pandas(file):
    try:
        data = pd.read_csv(file)
        return data
    except Exception as e:
        print(f"Error loading data with Pandas: {e}")
        return pd.DataFrame()
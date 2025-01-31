import pandas
import matplotlib.pyplot
import pandas as pd

def load_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"File not found at {file_path}")
    except Exception as e:
        print(f"An error occurred{e}")

file_path= "/Users/callumsmith/PycharmProjects/PythonProject/Unit1_Fundamentals/Fundamentals1/womenInSTEM.csv"
data = load_csv(file_path)

if data is not None:
    print(data)



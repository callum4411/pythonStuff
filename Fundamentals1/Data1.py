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


# Converts a sheet into a DataFrame
def sheetToDataFrame(worksheet):
  dataFrame = pandas.DataFrame(worksheet.get_all_values())
  dataFrame.columns = dataFrame.iloc[0]                # Assigns the first row as header
  dataFrame = dataFrame.drop(dataFrame.index[0])       # Drops the header from the dataframe
  dataFrame = dataFrame.reset_index(drop=True)         # Resets the index to show the original data arrangement
  return dataFrame

# Converts column to numeric values
def convertColumnNumeric(dataFrame, columnName):
  dataFrame[columnName] = pandas.to_numeric(dataFrame[columnName])

# Sorts a DataFrame with the given parameters
def sortDataFrame(dataFrame, columnName, isAscending, numOfElements):
  return dataFrame.sort_values(by=columnName, ascending=isAscending).head(numOfElements)

# Convert the womenInSTEM sheet to a DataFrame
dataFrame = sheetToDataFrame(data)

# Convert two of columns to numeric values
convertColumnNumeric(dataFrame, "Men")
convertColumnNumeric(dataFrame, "Women")

# Create a DataFrame with the top 10 elements because isAscending is False
# if isAcending were True, we would get the bottom 10
sortedTenDF = sortDataFrame(dataFrame, "Women", False, 10)

# Plotting using Pandas
graph = sortedTenDF.plot(kind="bar", x="Major", y=["Men", "Women"], color=["blue", "red"])

# Make the legend show only the columns containing y values
graph.legend()

# Labels and title
graph.set_xlabel("Majors")
graph.set_ylabel("Number of Students")
graph.set_title("Top 10 Majors by Number of Male and Female Students in STEM")

# Set the x-axis ticks and rotate x-axis labels
graph.set_xticklabels(sortedTenDF.get("Major"), rotation=90)

# Adjust layout and show the plot for better display
matplotlib.pyplot.tight_layout()
matplotlib.pyplot.show()
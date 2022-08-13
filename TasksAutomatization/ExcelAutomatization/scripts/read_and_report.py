import pandas as pd
from path_helps import get_path

def main():
    # Get path of the Excel File
    excel_name = input("Type the Excel File:")
    if not excel_name.endswith(".xlsx"):
        excel_name += ".xlsx"
    excel_path = get_path(excel_name, "input")
    
    # Specify columns to read
    input_cols = [i for i in range(3,8)].append(12)

    # Open and read the file (and the given sheet) with pandas
    dataframe = pd.read_excel(excel_path, "Sheet 1", header = 0, usecols=input_cols)

    # Receive the size of the table/data
    print(f"Size: {dataframe.shape}")
    print(f"Columns: {dataframe.columns}")

    # Print the info of some values of a given column
    print(f"Payment Info:{dataframe['Payment'].head(5)}")

    # Print a preview of the head of the different data
    data_columns = dataframe.columns
    for col in data_columns:
        print(dataframe[col].head(5))

    # Select and filter info
    dataframe[dataframe["Payment"]== "Cash"]
    print(dataframe["Payment"])

    # Export data
    csv_name = "payment_report.csv"
    csv_path = get_path(csv_name, "input")
    dataframe.to_csv(csv_path, "output", sep= ",", header = True, index = False)

if __name__ == "__main__":
    main()
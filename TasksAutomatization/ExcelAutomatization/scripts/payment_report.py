"""
Base code by: DATA SCIENCE PROJECT
Link: https://youtu.be/JL9RMCS4Sho?list=PLxYZ6JuFZuoYsbJuR_ukb0w1Yz4HlUq_c
Modified and commented by: Daniel Lopez
"""

import pandas as pd
from path_helps import get_path


def read_file(excel_name):
    """
    Read an Excel file using pandas
    Input:
        excel_name --> Name of the Excel file to read and process
    Output:
        dataframe --> Data contained in the Excel file read
    """
    if not excel_name.endswith(".xlsx"):
        excel_name += ".xlsx"
    excel_path = get_path(excel_name, "input")

    input_cols = [i for i in range(3, 8)].append(12)

    dataframe = pd.read_excel(excel_path, "Sheet 1", header=0, usecols=input_cols)
    return dataframe


def filter_info(dataframe, category, filter):
    """
    Filter the information given the dataframe and the category
    Input:
        dataframe --> Data of the Excel read
        category --> Column you want to filter
        filter --> Param to classify in the column
    Output:
        dataframe --> Data of the Excel read but filtered
    """
    dataframe[dataframe[category] == filter]
    print(f"Results of the filter:\n{dataframe[category]}")
    return dataframe


def export_csv(dataframe):
    """
    Export data from the dataframe to a csv_file
    Input:
        dataframe --> Data of the Excel you want to export
    """
    csv_name = "payment_report.csv"
    csv_path = get_path(csv_name, "output")
    dataframe.to_csv(csv_path, "output", sep=",", header=True, index=False)


def main():
    """
    Generate a report of a supermarket, according to the payment option.
    """
    excel_name = input("Type the Excel File name to read:")
    dataframe = read_file(excel_name)

    dataframe = filter_info(dataframe, "Payment", "Cash")

    export_csv(dataframe)


if __name__ == "__main__":
    main()

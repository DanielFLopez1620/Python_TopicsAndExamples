import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference

# TODO: Generate functions for pandas and openpyxl
def main():
    # PANDA SECTION 1:
    # Import data from Excel
    # FIXME: Add path to the mini project
    data_file = "supermarket_sales.xlsx"
    data_imported = pd.read_excel(data_file)
    data_imported[["Gender", "Product line", "Total"]]

    # Create pivot table:
    data_resume = data_imported.pivot_table(index="Gender", columns="Product line", values="Total", aggfunci='sum').round(0)

    # Export to Excel:
    data_resume.to_excel("sales_2022.xlsx", startrow=4,sheet_name="Report")

    # OPENPYXL SECTION 1:
    # Reading data from Excel:
    excel_data = load_workbook("sales_2022.xlsx")
    excel_sheet = excel_data["Report"]

    # Obtain data workspace of the data_sheet
    min_column = excel_data.active.min_column
    max_column = excel_data.active.max_column
    min_row = excel_data.active.min_row
    max_row = excel_data.active.max_row

    # Insert a graphic:
    # barchat = BarChart() <-- Continue here


if __name__ == "__main__":
    main()
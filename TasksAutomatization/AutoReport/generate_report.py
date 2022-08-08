from importlib.resources import path
import openpyxl
import pandas as pd
from openpyxl import Workbook, load_workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.styles import Font
import string
from path_helps import get_path_dir
import os

def main():
    # PANDA SECTION:
    # Import data from Excel
    path_file = get_path_dir("TasksAutomatization", "AutoReport")
    data_file = os.path.join(path, "supermarket_sales.xlsx")
    data_imported = pd.read_excel(data_file)
    data_imported[["Gender", "Product line", "Total"]]

    # Create pivot table:
    data_resume = data_imported.pivot_table(index="Gender", columns="Product line", values="Total", aggfunci='sum').round(0)

    # Export to Excel:
    data_resume.to_excel("sales_2022.xlsx", startrow=4,sheet_name="Report")

    # OPENPYXL SECTION:
    # Reading data from Excel:
    excel_data = load_workbook("sales_2022.xlsx")
    excel_sheet = excel_data["Report"]

    # Obtain data workspace of the data_sheet
    min_column = excel_data.active.min_column
    max_column = excel_data.active.max_column
    min_row = excel_data.active.min_row
    max_row = excel_data.active.max_row

    # Get reference for a graphic
    barchart = BarChart()
    data = Reference(excel_sheet, min_col=min_column+1, max_col=max_column, min_row = min_row, max_row = max_row)
    info = Reference(excel_sheet, min_col=min_column, max_col=min_column, min_row = min_row+1, max_row = max_row)
    
    # Add data and categories to the graphic
    barchart.add_data(data, titles_from_data=True)
    barchart.insert_categories(info)

    # Insert and edit style of the graphic
    excel_sheet.add_chart(barchart, "B12")
    barchart.style = 5
    barchart.title = "Sells"
    
    # Insert formula and format in specific cell
    excel_sheet["B8"] = "=SUM(B6:B7)"
    excel_sheet["B8"].style = "Currency"

    # Adding format to multiples cell
    letters = list(string.ascii_uppercase)
    letters_excel = letters[0:max_column]
    for i in letters_excel:
        if i == "A":
            continue
        excel_sheet[f"{i}{max_column+1}"].style = "Currency"
        excel_sheet[f"{i}{max_column+1}"] = f"=SUM({min_column+1}:{max_column})"
    excel_sheet[f'{letters_excel[0]}{max_row+1}'] = "Total"

    # Add format to the Excel file
    excel_sheet["A1"] = "Report"
    excel_sheet["A2"] = "2022"
    excel_sheet["A1"].font = Font("Arial", bold=True, size=20 )
    excel_sheet["A2"].font = Font("Arial", bold=True, size=12 )

    # Save barchart into the excel sheet and document
    excel_data.save("sales_2022.xlsx")



if __name__ == "__main__":
    main()
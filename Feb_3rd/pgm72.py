#WRITING DATA FROM EXCEL
import openpyxl

wb=openpyxl.load_workbook("F:\selenium_pgms_BhanuSir\Book1.xlsx")
sheet1=wb['Sheet1']
sheet1.cell(1,1).value="Neetha"
wb.save("F:\selenium_pgms_BhanuSir\Book2.xlsx")
wb.close()


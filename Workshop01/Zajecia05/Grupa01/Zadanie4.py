'''
Created on 11 sie 2016

@author: dadas
'''

from openpyxl import Workbook
from openpyxl.styles.fonts import Font
from openpyxl.styles import colors
from openpyxl.reader.excel import load_workbook

location = "IntegrationTestsControl_CONN.xlsx"

wb = load_workbook(location)
ft = Font(name="Calibri",size=11,color=colors.RED)
ws = wb.active

for row in ws.rows:
    for cell in row:
        if (cell.value == "NOT TESTED"):
            cell.font = ft

wb.save(location)

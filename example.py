import shutil
import openpyxl

shutil.copy2('path1.xlsx', 'path2.xlsx')

book = openpyxl.load_workbook('path2.xlsx')
try:
    sheet = book['Sheet1']
    sheet['B2'].value = 'hoge'
    book.save('path2.xlsx')
finally:
    book.close()

import openpyxl
path = "C:\\Users\\SHINY\\OneDrive\\Desktop\\excel\\hello.xlsx"   
wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active
cell_obj = sheet_obj['a1':'b7']
for cell1, cell2 in  cell_obj:
    print(cell1.value,cell2.value) 
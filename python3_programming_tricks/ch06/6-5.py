import xlrd
book = xlrd.open_workbook('demo.xlsx')
book.sheets()
sheet =  book.sheet_by_index(0)
c00 = sheet.cell(0, 0)
c00.ctype
c00.value
xlrd.XL_CELL_TEXT
xlrd.XL_CELL_NUMBER
sheet.cell_value(1,1)
sheet.cell_value(0,0)
sheet.row(0)
sheet.row_values(0)
sheet.row_values(1,1)
sheet.put_cell(0,sheet.ncols,xlrd.XL_CELL_TEXT,'总分',None)

# 写入excel

import xlwt

wbook = xlwt.Workbook()
wsheet = wbook.add_sheet('test')
wsheet.write(0,0,'abc')
wsheet.write(0,1,100)
wbook.save('test.xlsx')

import xlrd, xlwt

xlrd.open_workbook('demo.xlsx')
rsheet = rbook.sheet_by_index(0)
k = rsheet.ncols
rsheet.put_cell(0,k,xlrd.XL_CELL_TEXT,'总分',None)

for i in range(1, rsheet.nrows):
    t = sum(rsheet.row_values(i, 1))
    rsheet.put_cell(i,k,xlrd.XL_CELL_NUMBER,t,None)


xlwt.Workbook()

wsheet = wbook.add_sheet(rsheet.name)
for i in range(rsheet.nrows):
    for j in range(rsheet.ncols):
        wsheet.write(i,j,rsheet.cell_value(i,j))


wbook.save('out.xlsx')



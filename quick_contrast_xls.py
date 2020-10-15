# author: s-kline
# quick-and-dirty way to write excel files with contrast info in each SPM second level directory, needed for batched ROI analysis
# only works if the second level model has these exact contrasts, 1: positive result, 2: negative result
# e.g. t-tests or simple regressions with one variable


import xlsxwriter
import os

path = 'Y:\\0202RS\\work\\auswertung\\slevel_SID\\model01\\'
content = os.listdir(path)

for folder in content:
    contrast_list = []
    comps = str.split(folder, '_')
    name = ('_'.join(comps[:len(comps)-1]))
    contrast_list = [1, 'PosResult_' + name,
                     2, 'NegResult_' + name]
    print(contrast_list)
    workbook = xlsxwriter.Workbook(path + folder + '\Kontraste.xlsx')
    worksheet = workbook.add_worksheet()

    worksheet.write('A1', contrast_list[0])
    worksheet.write('B1', contrast_list[1])
    worksheet.write('A2', contrast_list[2])
    worksheet.write('B2', contrast_list[3])

    workbook.close()
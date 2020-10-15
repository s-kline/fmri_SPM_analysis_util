# author: s-kline
# more robust way to write excel files with contrast info in second level directories.
# looks for contrast info in the second level batch files
# batch files must have the same name as the resulting slevel directory

import xlsxwriter
import os

contrast_list = []
#path = 'D:\\0179rs\\slevel\\'
#path = 'O:\\Stark\\Projekte Sexuelle Responsivität\\0179RS- Antizipation von sex Reizen\\Auswertung Sanja Klein\\secondlevel\\fertig_zum_laufenlassen\\'
#path = 'O:\\Kruse\\0205ok\\slevel\\t1\\PPI\\'
#batchpath = 'O:\\Kruse\\0205ok\\batches_slevel\\t1\\PPI\\'
#batchpath = 'O:\Stark\Projekte Sexuelle Responsivität\\0179RS- Antizipation von sex Reizen\Auswertung Sanja Klein\secondlevel\\batches\\'

path = 'Y:\\0202RS\\work\\auswertung\\slevel_SID\\model02\\'
batchpath = 'Y:\\0202RS\\work\\auswertung\\slevel_batches\\SID\\model02\\'

# path = 'Y:\\0205OK\\work\\auswertung\\slevel\\t1\\model01\\'
# batchpath = 'Y:\\0205OK\\work\\auswertung\\slevel_batches\\'

content = os.listdir(path)
#print(content)

for folder in content:
    print(folder)
    print(batchpath + folder)
    try:
        batchfile = open(batchpath + folder + '.m', 'r')

        for current_line in batchfile:
            if '.tcon.name' in current_line:
                contrast_number = current_line.split('tcon.name')[0]
                contrast_number = contrast_number[len(contrast_number)-3]
                contrast_list.append(int(contrast_number))

                contrast_name = current_line.split(" = '")[1]
                contrast_name = contrast_name[0:len(contrast_name)-3]

                if contrast_name == 'PosResult' or contrast_name == 'NegResult':
                    contrast_name += ('_'+ folder)

                contrast_list.append(contrast_name)

        batchfile.close()
        print(contrast_list)

        workbook = xlsxwriter.Workbook(path+folder+'\Kontraste.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', contrast_list[0])
        worksheet.write('B1', contrast_list[1])
        worksheet.write('A2', contrast_list[2])
        worksheet.write('B2', contrast_list[3])

        if len(contrast_list) > 4:
            worksheet.write('A3', contrast_list[4])
            worksheet.write('B3', contrast_list[5])
            worksheet.write('A4', contrast_list[6])
            worksheet.write('B4', contrast_list[7])

        workbook.close()

        workbook.close()

        contrast_list = []
    except:
        print('No matching batchfile in this folder for ' + folder)
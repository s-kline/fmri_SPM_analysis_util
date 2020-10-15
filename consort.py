# author: s-kline
# add a subject ID prefix to SPM first level contrast files so they can be saved in one directory
# can be used to give only specific contrasts of each participant to students, collaborators etc 

import os

# path = 'Y:\\0205OK\\work\\Abschlussarbeiten\\cons\\subjects\\model01_t2\\'
# path = 'Y:\\0205OK\\work\\Abschlussarbeiten\\cons\\subjects\\model01_t3\\'
# path = 'D:\\0188ok\\CANLab_Auswertungen\\allcons\\tag3_picpercept\\'
path = 'Y:\\0202RS\\work\\Abschlussarbeiten\\cons\\model_01\\'

# for bids directories:
for subject in os.listdir(path):
    cons = [i for i in os.listdir(path + subject) if i.startswith('con')]
    # print(subject[:8])
    [os.rename(path + subject + '\\' + name , path + subject + '\\' + subject[:8] + name) for name in cons]


# for subject in os.listdir(path):
    # cons = [i for i in os.listdir(path + subject) if i.startswith('con')]
    # print(subject[7:11])
    # [os.rename(path + subject + '\\' + name , path + subject + '\\' + subject[7:11] + name) for name in cons]

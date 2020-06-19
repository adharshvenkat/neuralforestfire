# -*- coding: utf-8 -*-
"""
Created on Sat May  2 12:46:52 2020

@author: Adharsh Venkatachalam
"""

#%%

#Preprosessing and readin of information from the dataset
import csv

FFMC=[]
DMC=[]
DC=[]
ISI=[]
temp_dev=[]
rh_dev=[]
temp_dev_nor=[]
rh_dev_nor=[]
fire_prob=[]

with open(r'C:\Users\Adharsh\OneDrive\Documents\Personal\Capstone Project\forestfires.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        FFMC.append(row[4])
        DMC.append(row[5])
        DC.append(row[6])
        ISI.append(row[8])
        
FFMC = FFMC[20:25]
DMC = DMC[20:25]
DC = DC[20:25]
ISI = ISI[20:25]

for i in range(len(FFMC)):
    FFMC[i] = float(FFMC[i])
    DMC[i] = float(DMC[i])
    DC[i] = float(DC[i])
    ISI[i] = float(ISI[i])

length = len(FFMC)
#%%

para_FWI_test = []

for i in range(length):
    para_FWI_test.append([])

for i in range(length):
    para_FWI_test[i].append(FFMC[i])
    para_FWI_test[i].append(DMC[i])
    para_FWI_test[i].append(DC[i])
    para_FWI_test[i].append(ISI[i])
    para_FWI_test[i].append(pred_BUI[i][0])

para_FWI_test = np.array(para_FWI_test)
    

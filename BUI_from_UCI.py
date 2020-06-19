# -*- coding: utf-8 -*-
"""
Created on Mon May  4 13:05:41 2020

@author: Adharsh Venkatachalam
"""

#%%
import csv

import numpy as np

import matplotlib.pyplot as plt

from keras.optimizers import Adam

from keras.models import Sequential

from keras.layers import Dense

from sklearn.model_selection import train_test_split

#%%

DMC_UCI = []
DC_UCI = []
add1_UCI = []
DMC = []
DC = []
add1 = []
BUI = []


with open(r'C:\Users\Adharsh\OneDrive\Documents\Personal\Capstone Project\forestfires.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        DMC_UCI.append(row[5])
        DC_UCI.append(row[6])
        add1_UCI.append(row[7])


DMC_UCI = DMC_UCI[20:25]
DC_UCI = DC_UCI[20:25]
add1_UCI = add1_UCI[20:25]


for i in range(len(DMC_UCI)):
    DMC_UCI[i] = float(DMC_UCI[i])
    DC_UCI[i] = float(DC_UCI[i])
    add1_UCI[i] = float(add1_UCI[i])
    
para_BUI_test = []

for i in range(len(DMC_UCI)):
    para_BUI_test.append([])

for i in range(len(DMC_UCI)):
    para_BUI_test[i].append(DMC_UCI[i])
    para_BUI_test[i].append(DC_UCI[i])
    para_BUI_test[i].append(add1_UCI[i])
    
para_BUI_test = np.array(para_BUI_test)


with open(r'C:\Users\Adharsh\OneDrive\Documents\Personal\Capstone Project\new_para_bui.csv') as file:
    reader = csv.reader(file)
    for row in reader:
        DMC.append(row[0])
        DC.append(row[1])
        add1.append(row[2])
        BUI.append(row[5])


for i in range(len(DMC)):
    DMC[i] = float(DMC[i])
    DC[i] = float(DC[i])
    add1[i] = float(add1[i])
    BUI[i] = float(BUI[i])
    

para_train_BUI = []


for i in range(len(DMC)):
    para_train_BUI.append([])
    
for i in range(len(DMC)):
    para_train_BUI[i].append(DMC[i])
    para_train_BUI[i].append(DC[i])
    para_train_BUI[i].append(add1[i])



fire_data = {'parameters': np.array(para_train_BUI), 'target': np.array(BUI)}

    

                                                         
X_train, X_test, Y_train, Y_test = train_test_split(fire_data['parameters'], fire_data['target'], random_state = 0)



#%%

model = Sequential()


model.add(Dense(60, input_dim=3, activation='relu'))

model.add(Dense(20, activation='relu'))

model.add(Dense(10, activation='relu'))

model.add(Dense(1, activation='relu'))

model.compile(loss = 'mse', optimizer = 'adam')

model.summary()

#%%

history = model.fit(X_train, Y_train, epochs = 4000) 

#%%

pred_BUI = model.predict(para_BUI_test)

print(pred_BUI)


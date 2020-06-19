# -*- coding: utf-8 -*-
"""
Created on Sun May  3 16:29:00 2020

@author: Adharsh Venkatachalam

"""
#%%

#Importing libraries 

import numpy as np

from keras.models import Sequential

from keras.layers import Dense

from sklearn.model_selection import train_test_split

#%%

fire_data = {'parameters': np.array([[97.06, 68.55, 408.55, 22.45, 114.03],
                                  [96.94, 68.06, 405.45, 21.88, 105.58],
                                  [96.76, 67.03, 390.06, 21.79, 100.74],
                                  [96.45, 66.61, 387.03, 20.16, 98.81],
                                  [93.36, 63.39, 384.23, 20.01, 90.23],
                                  [91.21, 61.10, 359.32, 18.59, 76.03],
                                  [90.20, 57.29, 355.65, 18.50, 72.81],
                                  [88.18, 55.61, 350.74, 18.76, 70.48],
                                  [87.61, 41.23, 248.45, 10.35, 51.26],
                                  [85.05, 40.87, 245.35, 9.56, 51.06],
                                  [73.16, 19.63, 73.60, 1.57, 23.27],
                                  [73.12, 18.40, 72.70, 1.28, 20.50],
                                  [72.22, 18.30, 71.93, 1.25, 20.37],
                                  [71.88, 16.27, 62.43, 1.13, 20.30],
                                  [69.95, 16.23, 61.83, 1.11, 19.00],
                                  [69.20, 15.03, 61.63, 1.10, 17.63],
                                  [68.03, 14.90, 57.10, 1.09, 17.57],
                                  [65.60, 13.33, 52.00, 1.06, 16.90],
                                  [64.18, 13.23, 45.17, 0.98, 15.80],
                                  [60.86, 12.53, 43.33, 0.78, 13.20]]),
             'target': np.array([61.75, 60.54, 60.48, 59.16, 57.85, 55.65,
                              54.82, 53.18, 52.29, 44.44, 26.62, 24.28, 
                              23.39, 21.15, 20.80, 18.16, 13.53, 11.40,
                              10.84, 10.60])}


X_train, X_test, Y_train, Y_test = train_test_split(fire_data['parameters'], fire_data['target'], random_state = 0)


#%%

model = Sequential()


model.add(Dense(200, activation='relu', input_dim=5))


model.add(Dense(40, activation='relu'))


model.add(Dense(20, activation='relu'))


model.add(Dense(1, activation='relu'))


model.compile(loss = 'mse', optimizer='adam')

history = model.fit(X_train, Y_train, epochs = 3500)

#%%

model.summary()

pred_FWI = model.predict(para_FWI_test)

print(pred_FWI)





# -*- coding: utf-8 -*-
"""fproject ML.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KkDrIevG8Qqb5m2B8voN898Qb3D9Wm07
"""

import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.feature_selection import SelectKBest, mutual_info_classif
from keras.models import Sequential
from keras.layers import Dense

data = load_breast_cancer()
X = data.data
y = data.target

df = pd.DataFrame(data=np.c_[X, y], columns=np.append(data.feature_names, 'target'))

print(df.describe())

k_best = SelectKBest(score_func=mutual_info_classif, k=15)
X_selected = k_best.fit_transform(X, y)

correlation_matrix = pd.DataFrame(X_selected, columns=data.feature_names[k_best.get_support()]).corr()
print("Correlation Matrix:")
print(correlation_matrix)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

from keras import layers
model = Sequential()
model.add(layers.Dense(256, activation='relu', name='Layer_1', input_shape=(X_train.shape[1],)))
model.add(layers.Dense(32, activation='relu', name='Layer_2'))
model.add(layers.Dense(1, activation='sigmoid', name='Output_Layer'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(X_train_scaled, y_train, epochs=20, batch_size=64)

test_loss, test_accuracy = model.evaluate(X_test_scaled, y_test)
print("Test Loss:", test_loss)
print("Test Accuracy:", test_accuracy)
#!/usr/bin/env python


import skops.io as sio
import argparse
# import pandas as pd
import polars as pl
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn import preprocessing


import warnings
warnings.filterwarnings('ignore')


from os import mkdir
from os import path
from sys import exit

parser = argparse.ArgumentParser(description='trenowanie modelu')
parser.add_argument('FROM', metavar='FROM', type=str, nargs=1,help='ścieżka do pliku z danymi')
parser.add_argument('TO', metavar='TO', type=str, nargs=1,help='ścieżka do pliku wynikowego (modelu)')

args=parser.parse_args()
FROM=args.FROM[0]
TO=args.TO[0]

#Wczytanie pliku
df=pl.read_csv(FROM)

#wyodrębnienie zmiennej zależnej
Y=df.drop_in_place("Client")

#podział na część testową i treningową
X_train, X_test, y_train, y_test = train_test_split(df,Y, test_size=0.80, random_state=2137)

#standaryzacja zmiennych
scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

param_grid = [    
    {'penalty' : ['l1', 'l2', 'elasticnet', None],
    'C' : np.logspace(-4, 4, 20),
    'solver' : ['lbfgs','newton-cholesky','newton-cg','liblinear','sag','saga'],
    'max_iter' : [100, 1000,2500, 5000]
    }
]

logModel=LogisticRegression()


clf = GridSearchCV(logModel, param_grid = param_grid, cv = 3, n_jobs=-1,verbose=4)

clf.fit(X_train,y_train)

print("Tuned Hyperparameters :", clf.best_params_)
print("Accuracy :",clf.best_score_)

sio.dump(clf,TO)

#zamiana stringów na int

#raport końcowy

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from Tree import DecisionTree as dt


def data_cleaning(df):
    df.insert(1, 'BUY_PRICE', df['BUYING'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
    df.insert(3, 'MAIN_PRICE', df['MAINT'].map({'vhigh': 0, 'high': 1, 'med': 2, 'low': 3}).astype(int))
    df.insert(5, 'DOOR', df['DOORS'].map({'2': 2, '3': 3, '4': 4, '5more': 5}).astype(int))
    df.insert(7, 'PASSENGER', df['PERSON'].map({'2': 2, '4': 4, 'more': 5}).astype(int))
    df.insert(9, 'LUG', df['LUGBOOT'].map({'small': 0, 'med': 1, 'big': 2}).astype(int))
    df.insert(11, 'SAFE', df['SAFETY'].map({'low': 0, 'med': 1, 'high': 2}).astype(int))
    df.insert(13, 'DECISION', df['CLASS'].map({'unacc': 0, 'acc': 1, 'good': 2, 'vgood': 3}).astype(int))
    data = df.drop(['BUYING', 'MAINT', 'LUGBOOT', 'DOORS', 'PERSON', 'SAFETY', 'CLASS'], axis = 1)

    return data

def shuffle(df, axis = 1):
    df = df.copy()
    df = df.reindex(np.random.permutation(df.index))
    return df

def split(df):
    df = np.array_split(df, 2)
    return df
df = pd.read_csv('Car.csv', header=None, names=['BUYING','MAINT', 'DOORS', 'PERSON', 'LUGBOOT', 'SAFETY', 'CLASS'])
rec = df.shape[0]
df = data_cleaning(df)
#df = shuffle(df)
#df = split(df)
t = dt()
t.fit(df)
print t


import numpy as np
import os
import sys
import math as mth
import pandas as pd
import matplotlib.pyplot as plt
np.set_printoptions(threshold=sys.maxsize)


def squareFunc():
    x = []
    for i in range(100):
        if mth.sin(i) > 0:
            x.append(1)
        else:
            x.append(0)
    return x

def sinFunc():
    y = []
    for i in range(100):
        if mth.sin(i) > 0:
            y.append(mth.sin(i))
        else:
            y.append(0)
    return y

def constantFunc():
    z = []
    for i in range(100):
        z.append(5)
    return z

def createData():
    data = np.zeros((150, 1))
    labels = np.zeros((150, 1))
    for i in range(0,150,3):
        if i <= 147:
            labels[i,0] = 1
            labels[i+1,0] = 2
            labels[i+2,0] = 3
            data[i] = sinFunc()
            data[i+1] = squareFunc()
            data[i+2] = constantFunc()
    labelDF = pd.DataFrame(labels)
    dataDF = pd.DataFrame(data)
    print(labelDF)
    print(dataDF)
    labelDF.to_csv("synthetic_data_labels.csv")
    dataDF.to_csv("synthetic_data.csv")



createData()




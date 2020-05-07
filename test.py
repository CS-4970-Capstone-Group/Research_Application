import keras
import numpy as np
import csv
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv1D, Dense, Flatten, Dropout, MaxPooling1D
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
from scipy.io import loadmat
import copy
import os


class Heart_Risk_Classifier():

    #prepare the data
    def extract_data(directory):
        arr = []
        arr = np.asarray(arr, dtype="double")

        for filename in os.listdir(directory):
            os.open(directory,os.O_RDONLY)
            with open(filename, "r") as file:
                print(os.getcwd())
                buffer = csv.reader(file)
                data_list = list(buffer)
                data = np.asarray(data_list, dtype="double")
                data = np.split(data, 10)
                data = np.asarray(data, dtype="double")
                data = np.squeeze(data, axis=2)
                file.close()
            arr = np.append(arr, copy.deepcopy(data))
        return arr

train_dir = r"C:\Users\bradb\Documents\training_data_copy"

hc = Heart_Risk_Classifier
arr = hc.extract_data(train_dir)
print(arr)
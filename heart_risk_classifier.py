import keras
import numpy as np
import csv
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Conv1D, Dense, Flatten, Dropout, MaxPooling1D
from keras.preprocessing.image import ImageDataGenerator
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
from scipy.io import loadmat
import copy
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

class Heart_Risk_Classifier():

    #prepare the data
    def extract_data(directory):
        arr = []
        arr = np.asarray(arr, dtype="double")

        for filename in os.listdir(directory):
            next = directory + '\\' + filename
            with open(next, "r") as file:
                buffer = csv.reader(file)
                data_list = list(buffer)
                data = np.asarray(data_list, dtype="double")
                data = np.split(data, 10)
                data = np.asarray(data, dtype="double")
                data = np.squeeze(data, axis=2)
                file.close()
            arr = np.append(arr, copy.deepcopy(data))
        return arr

    def extract_file(path):
        arr = []
        with open(path, "r") as file:
            buffer = csv.reader(file)
            data_list = list(buffer)
            data = np.asarray(data_list, dtype="double")
            data = np.split(data, 10)
            data = np.asarray(data, dtype="double")
        arr.append(copy.deepcopy(data))
        arr = np.asarray(arr, dtype="double")
        arr = np.squeeze(arr, axis=0)
        file.close()
        return arr

    #training
    def train_classifier(trainingData, trainingLabels, testData, testLabels):
        verbose = 0
        epochs = 10
        batch_size = 30
        model = Sequential()
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu', input_shape=(3000, 1)))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Conv1D(filters=1, kernel_size=100, activation='relu'))
        model.add(Dropout(0.5))
        model.add(MaxPooling1D(pool_size=5))
        model.add(Flatten())
        model.add(Dense(3000, activation='relu'))
        model.add(Dense(3000, activation='relu'))
        model.add(Dense(3000, activation='relu'))
        model.add(Dense(3000, activation='relu'))
        model.add(Dense(3000, activation='relu'))
        model.add(Dense(2, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model_output = model.fit(trainingData, trainingLabels, epochs=epochs, batch_size=batch_size, verbose=verbose)
        model.save("model.h5")
        prediction = model.predict_classes(testData)
        for i in range(len(testData)):
            print((testLabels[i], prediction[i]))
        print(model_output.history)
        _, accuracy = model.evaluate(testData, testLabels, batch_size=batch_size, verbose=verbose)
        #plt.plot(model_output.history['loss'])
        #plt.show()
        return accuracy


    def classify_risk(template, testData):
        if testData.shape == (3000,1):
            testData = np.expand_dims(testData, axis=0)
        elif testData.shape == (1,3000):
            testData = np.expand_dims(testData, axis=2)

        correct_shape = (1,3000,1)
        if testData.shape != correct_shape:
            print("wrong input shape")
            return -1
        else:
            #Add in pre-established weights
            model = load_model(template)#template parameter should just be "model.h5" with file in same directory as program

            #CLASSIFICATION
            prediction = model.predict_classes(testData)
            result = copy.deepcopy(prediction[0])
            return result

    def test_classify(self):
        return 0.5




def summarize_results(scores):
    print(scores)
    m = np.mean(scores)
    s = np.std(scores)
    print('Accuracy: %.3f%% (+/-%.3f)' % (m,s))





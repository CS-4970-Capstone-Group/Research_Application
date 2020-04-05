import keras
import numpy as np
import csv
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Dense, Flatten, Dropout, MaxPooling1D
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report

class Heart_Risk_Classifier():

    #prepare the data


    #training
    def classify_risk(data, weights):
        #Rebuild Model
        verbose = 0
        epochs = 20
        batch_size = 1
        model = Sequential()

        # Conv1D is the central part of this and is involved with a 1D classification attempt by the network
        model.add(Conv1D(filters=1, kernel_size=5, activation='relu', input_shape=(30000, 1)))
        model.add(Conv1D(filters=1, kernel_size=5, activation='relu'))
        model.add(Conv1D(filters=1, kernel_size=5, activation='relu'))
        model.add(Conv1D(filters=1, kernel_size=5, activation='relu'))

        # 'Dropout()' is a Keras function which adds 0's into the model so as to reduce the chance of overfitting
        model.add(Dropout(0.5))

        # Max pooling or the taking of a maximum as representative of a subset of a produced feature => Generalization
        model.add(MaxPooling1D(pool_size=2))

        # 'Flatten()' function is as it sounds. Flattens data into one array to be fed into traditional neural network
        model.add(Flatten())

        # 'Dense()' function is Keras equivalent call to a traditional neural network. Dense(number of outputs, activation)
        model.add(Dense(100, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(100, activation='relu'))
        model.add(Dense(4, activation='softmax'))  # output of 4 because one-hot encoding made 4 digit binary representations

        #Add in pre-established weights
        model.load_weights(weights)

        #CLASSIFICATION
        # 'compile()' function gets are "loss" from the classification CNN run (i.e. the degree to which the CNN was wrong)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        prediction = model.predict_classes(data)
        return prediction

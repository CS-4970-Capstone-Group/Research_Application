import keras
import numpy as np
import csv
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Conv1D, MaxPooling1D, Dense, Flatten, Dropout, MaxPooling1D
from matplotlib import pyplot as plt

#Created three classes of synthetic data(sinusoidal, condensed sinusoidal, and constant) to be classified by a 1D CNN
#Currently warnings from PyCharm IDE concerning deprecated functions, will resolve in future iteration of CNN

def cnn_model(trainingData, trainingLabels, testData, testLabels):
    #'verbose' is simply a Keras feature which displays a progress bar. Set to 0 as not that necessary for this CNN.
    verbose = 0

    #Number of epochs or times we want network to cycle between classification and learning. Too much = overfitting
    epochs = 25 #Settled on 25. Ultimately there is an optimal number (not too high or too low).
    #Batch size of 1 for online style of data input. Usually preferable. Will have to check with Dr. Keller.
    batch_size = 1
    model = Sequential()

    #Conv1D is the central part of this and is involved with a 1D classification attempt by the network
    model.add(Conv1D(filters=1, kernel_size=3, activation='relu', input_shape=(100, 1)))#each point as 100 values
    model.add(Conv1D(filters=1, kernel_size=3, activation='relu'))#only 1 filter for each as data is pretty arbitrary
    #As an example, if dealing with color images with Red-Green-Blue values, would want 3 filters ->one for each color.

    #'Dropout()' is a Keras function which adds 0's into the model so as to reduce the chance of overfitting
    model.add(Dropout(0.5))

    #Max pooling or the taking of a maximum as representative of a subset of a produced feature => Generalization
    model.add(MaxPooling1D(pool_size=2))

    #'Flatten()' function is as it sounds. Flattens data into one array to be fed into traditional neural network
    model.add(Flatten())

    #'Dense()' function is Keras equivalent call to a traditional neural network. Dense(number of outputs, activation)
    model.add(Dense(100, activation='relu'))
    model.add(Dense(4, activation='softmax')) #output of 4 because one-hot encoding made 4 digit binary representations

    #'compile()' function gets are "loss" from the classification CNN run (i.e. the degree to which the CNN was wrong)
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

    #Keras uses the 'fit' function to handle the process of backpropagation and by extension the learning of the CNN
    model.fit(trainingData, trainingLabels, epochs=epochs, batch_size=batch_size, verbose=verbose)
    _, accuracy = model.evaluate(testData, testLabels, batch_size=batch_size, verbose=verbose)
    return accuracy

#Used to define how accurate overall the CNN is after being trained after the prescribed number of epochs
def summarize_results(scores):
    print(scores)
    m = np.mean(scores)
    s = np.std(scores)
    print('Accuracy: %.3f%% (+/-%.3f)' % (m,s))


## MAIN ##----------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':

    #DATA RETRIEVAL AND PROCESSING
    trainingData = []
    trainingLabels = []
    testData = []
    testLabels = []

    #Retrieving a collection of synthetic data from CSV's created in another program.
    with open(r"C:\Users\bradb\Documents\Data_Producer\synthetic_data.csv", "r") as file:
        buffer = csv.reader(file)
        trainingList = list(buffer)

    with open(r"C:\Users\bradb\Documents\Data_Producer\synthetic_data_labels.csv", "r") as file2:
        buffer2 = csv.reader(file2)
        trainingLabelsList = list(buffer2)

    #Removing headers
    trainingList.pop(0)
    trainingLabelsList.pop(0)
    #Removing row labels
    for i in range(len(trainingList)):
        trainingList[i].pop(0)

    #Collecting 125 of the data points (which are arrays of 100 values) to be used towards training the network
    for j in range(125):
        trainingData.append(trainingList[j])

    #Storing other 25 data points in a separate list to be used for validation of the network's accuracy
    for k in range(125, 150):
        testData.append(trainingList[k])

    #Doing the same training and test/validation split up for the respective labels
    for m in range(125):
        trainingLabels.append(trainingLabelsList[m][1])

    for p in range(125, 150):
        testLabels.append(trainingLabelsList[p][1])

    #Converting the lists into numpy arrays which are expected of the Keras library
    trainingDataArray = np.asarray(trainingData)
    trainingDataArray = np.expand_dims(trainingDataArray, axis=2)#Dimensions are expanded per Keras requirements

    #Viewing the samples of each class to be learned by the CNN#--------------------------------------------------------
    plt.plot(trainingData[0])
    plt.title("sample: sinusoidal data class")
    plt.show()

    plt.plot(trainingData[1])
    plt.title("sample: condensed sinusoidal data class")
    plt.show()

    plt.plot(trainingData[2])
    plt.title("sample: constant data class")
    plt.show()
    # ------------------------------------------------------------------------------------------------------------------

    #'to_categorical()' function is used to transform the labels into a 'one-hot' encoding (i.e. binary representation)
    trainingDataLabels = np.asarray(trainingLabels, dtype = np.float)
    trainingDataLabels = to_categorical(trainingDataLabels) #class 1 becomes 0100, class 2 becomes 0010, etc, etc, etc

    testDataArray = np.asarray(testData)
    testDataArray = np.expand_dims(testDataArray, axis=2)

    testLabelArray = np.asarray(testLabels, dtype=np.float)
    testLabelArray = to_categorical(testLabelArray)

    scores = list()

    #OPERATION AND EVALUATION OF CNN
    for e in range(5):
        score = cnn_model(trainingDataArray, trainingDataLabels, testDataArray, testLabelArray)
        score = score*100.0
        print('>#%d: %.3f' % (e+1, score))
        scores.append(score)
    summarize_results(scores)
    #Been getting results between 85% and 90%, which is not bad per say, but could be better given the type of data



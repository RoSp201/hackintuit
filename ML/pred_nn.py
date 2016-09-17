from keras.utils import np_utils
from keras.models import Sequential
from keras.optimizers import SGD, Adagrad
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.regularizers import l2

from scipy.stats import mode
import numpy as np
import pickle

# Use neural net to predict salary from census data
# Must one-hot encode all categorical features

# Will eventually get the data from another file, after Bryan finishes the data processing
# from data_processing.py import X_train, Y_Train


#################################
# Model specification
# Start from an empty sequential model where we can stack layers
model = Sequential()
reg = l2(0.001)

## Add a fully-connected layer.
model.add(Dense(output_dim=50, input_dim=len(design.T), W_regularizer=reg))

## Add tanh activation function to each neuron
model.add(Activation("relu"))

## Add a fully-connected layer.
model.add(Dense(output_dim=50, input_dim=50, W_regularizer=reg))

## Add tanh activation function to each neuron
model.add(Activation("tanh"))

## Add another fully-connected layer with 2 neurons, one for each class of labels
model.add(Dense(output_dim=3, activation='softmax', W_regularizer=reg))
#################################

## Compile the model with categorical_crossentropy as the loss, and stochastic gradient descent (learning rate=0.001, momentum=0.5,as the optimizer)
model.compile(loss='categorical_crossentropy', optimizer=SGD(lr=0.01, momentum=0.5), metrics=['accuracy'])
# for l in model.layers: print(l.get_weights(), '\n')

## Fit the model (10% of training data used as validation set)
model.fit(X_train, y_train, nb_epoch=5, batch_size=1,validation_split=0.0, show_accuracy=True)


# Will mess around with hyperparameters tomorrow



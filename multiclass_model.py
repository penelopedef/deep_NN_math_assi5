from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.utils import to_categorical


def define_dense_model_single_layer(input_length, activation_f='sigmoid', output_length=1):
    """Define a dense model with a single layer with the following parameters:
    input_length: the number of inputs
    activation_f: the activation function
    output_length: the number of outputs (number of neurons)"""
    model = keras.Sequential()
    # Add a Dense layer input length, activation function, and output length
    model.add(Dense(units=output_length, input_dim=input_length, activation=activation_f))
    return model

def define_dense_model_with_hidden_layer(input_length, 
                                         activation_func_array=['relu','sigmoid'],
                                         hidden_layer_size=10,
                                         output_length=1):
    """Define a dense model with a hidden layer with the following parameters:
    input_length: the number of inputs
    activation_func_array: the activation function for the hidden layer and the output layer
    hidden_layer_size: the number of neurons in the hidden layer
    output_length: the number of outputs (number of neurons in the output layer)"""

    model = keras.Sequential()

    # Add the input layer
    model.add(Dense(units=hidden_layer_size, input_dim=input_length, activation=activation_func_array[0]))

    # Add the combined hidden and output layer with activation function and output length
    model.add(Dense(units=output_length, activation=activation_func_array[1]))

    return model



def get_mnist_data():
    """Get the MNIST data."""
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    x_train = x_train.reshape(60000, 784).astype('float32') / 255
    x_test = x_test.reshape(10000, 784).astype('float32') / 255 
    return (x_train, y_train), (x_test, y_test)

def fit_mnist_model(x_train, y_train, model, epochs=2, batch_size=2):
    """Fit the model to the data.
    compile the model and add parameters for  the "optimizer", the loss function, 
    and the metrics, Hint: use categorical crossentropy for the loss function .

    then fit the model on the training data. (pass the epochs and batch_size params)
    """

    # One-hot encode the target labels
    y_train_one_hot = to_categorical(y_train, num_classes=10)

    # Compile the model with categorical crossentropy loss, Adam optimizer, and accuracy metric
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    # Fit the model on the training data
    model.fit(x_train, y_train_one_hot, epochs=epochs, batch_size=batch_size)    
    return model
  
def evaluate_mnist_model(x_test, y_test, model):
    """Evaluate the model on the test data.
    Hint: use model.evaluate() to evaluate the model on the test data.
    """
    # One-hot encode the target labels
    y_test_one_hot = to_categorical(y_test, num_classes=10)

    # Evaluate the model on the test data
    loss, accuracy = model.evaluate(x_test, y_test_one_hot)
    return loss, accuracy


# Introduction
---
This code demonstrates how to train a neural network using the Keras library to classify three classes based on three input features. The input data `X` has four observations, each consisting of three input features, and the target data `y` has three output classes. The neural network architecture includes an input layer, a hidden layer, and an output layer. The activation function used for the hidden layer is a sigmoid function, and for the output layer, we use a softmax function.

### Dependencies
---
This code requires the Keras library and the NumPy library, which can be installed via `pip`:
~~~
$ pip install keras numpy
~~~
---

### Usage
To run the code, simply execute the main.py file:

~~~
$ python main.py
~~~
---
This will train the neural network on the input and target data, with 1000 epochs and a batch size of 4. The accuracy of the trained model will then be printed to the console.

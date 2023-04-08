# Import the necessary modules
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Define the input and output data
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]])  # 3 input array
y = np.array([[1, 0, 0], [0, 1, 0], [0, 1, 0], [1, 0, 0]])


# Define the neural network architecture
model = Sequential()
model.add(Dense(4, input_dim=3, activation='sigmoid'))
model.add(Dense(3, activation='softmax'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(X, y, epochs=1_000, batch_size=4)

# Evaluate the model
scores = model.evaluate(X, y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, AveragePooling2D
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = cifar10.load_data()

# Preprocess data
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255
y_train = to_categorical(y_train, num_classes=10)
y_test = to_categorical(y_test, num_classes=10)

# Function to create CNN model
def create_model(pooling_type='max'):
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(32, 32, 3)))
    if pooling_type == 'max':
        model.add(MaxPooling2D((2, 2)))
    elif pooling_type == 'average':
        model.add(AveragePooling2D((2, 2)))
    else:
        raise ValueError("Invalid pooling type")
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(10, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
    return model

# Create models with different pooling types
model_max_pooling = create_model('max')
model_average_pooling = create_model('average')

# Train models
history_max = model_max_pooling.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))
history_average = model_average_pooling.fit(x_train, y_train, epochs=10, validation_data=(x_test, y_test))

# Evaluate models
test_loss_max, test_acc_max = model_max_pooling.evaluate(x_test, y_test)
test_loss_average, test_acc_average = model_average_pooling.evaluate(x_test, y_test)
print("Max Pooling Test Accuracy:", test_acc_max)
print("Average Pooling Test Accuracy:", test_acc_average)

# Visualize training history
plt.plot(history_max.history['accuracy'], label='Max Pooling')
plt.plot(history_average.history['accuracy'], label='Average Pooling')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
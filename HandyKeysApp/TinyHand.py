import tensorflow as tf
from tensorflow.keras.preprocessing import image
import cv2 as cv
import numpy as np
import os

class TinyHand():
    """This class is responsible for utlizing a tensorflow model to decide if a key is pressed or not."""
    def __init__(self, weights_file):
        image_size = 256
        self.tiny_hand = tf.keras.models.Sequential([

        #First Layer, First Layer remains the same
        tf.keras.layers.Conv2D(64, (3,3), activation='relu',padding='same', input_shape=(image_size, image_size, 3)),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Dropout(0.2), #Indroducing Dropout Layers which improves regularization

        #Second Layer, Convolution with depth 32
        tf.keras.layers.Conv2D(32, (3,3),padding='same', activation='relu'),
        tf.keras.layers.Conv2D(32, (3,3),padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Dropout(0.2), #Indroducing Dropout Layers which improves regularization 

        #Third Layer, Convolution with depth 64
        tf.keras.layers.Conv2D(64, (3,3),padding='same', activation='relu'),
        tf.keras.layers.Conv2D(64, (3,3),padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Dropout(0.2), #Indroducing Dropout Layers which improves regularization

        #Fourth Layer, Convolution with depth 128 Increasing the count of Conv to 3
        tf.keras.layers.Conv2D(128, (3,3),padding='same', activation='relu'),
        tf.keras.layers.Conv2D(128, (3,3),padding='same', activation='relu'),
        tf.keras.layers.Conv2D(128, (3,3),padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Dropout(0.2), #Indroducing Dropout Layers which improves regularization 

        #Fifth Layer, Convolution with depth 256
        tf.keras.layers.Conv2D(256, (3,3),padding='same', activation='relu'),
        tf.keras.layers.Conv2D(256, (3,3),padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),

        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(2048, activation='relu'),
        tf.keras.layers.Dense(8, activation='softmax')])

        #Load the weights
        self.tiny_hand.load_weights(weights_file)


    def predict(self,img):
        """
        This function is responsible for predicting the key pressed.
        """
        #convert the image to rgb
        array_img = np.expand_dims(img, axis=0)
        images = np.vstack([array_img])
        classes = self.tiny_hand.predict(images, batch_size=1)
        print(classes)

        max_index = np.argmax(classes[0])
        
        # switch case from 0 to 7
        switcher = {
            0: "Key_1",
            1: "Key_2",
            2: "Key_3",
            3: "Key_4",
            4: "Key_5",
            5: "Key_6",
            6: "Key_7",
            7: "NONE"
        }
        return switcher.get(max_index, "Invalid Key")
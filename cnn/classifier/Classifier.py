from email.mime import image
import tensorflow as tf
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras import utils
CATEGORIES = ["500","2000"]
import os
from time import sleep
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import streamlit as st
from PIL import Image
def frontLoad():
    print("Loading Front Classifier Model ....\n\n")
    classifier = tf.keras.models.load_model("modelfront")
    print("\n\nFront Classifier Model Loaded.\n\n")
    return classifier
def backLoad():
    print("Loading Back Classifier Model ....\n\n")
    classifier = tf.keras.models.load_model("modelback")
    print("\n\nBack Classifier Model Loaded.\n\n")
    return classifier

def currency_classification(img, model):
    
    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    image = Image.open(img)
    #image sizing
    size = (224, 224)

    image = ImageOps.fit(image, size, Image.ANTIALIAS)


    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    return np.argmax(prediction)


if __name__=='__main__':
    classifier=frontLoad()
    sleep(2)
    os.system('clear')
    filepath=input("Enter Front Side of Note:")
    label1=currency_classification(filepath,classifier)
    switcher = {
             0 : "five hundred", 
             1: "two thousand",
             2: "invalid image",
    }
    s1=switcher.get(label1, "Not Maching") 
    print(s1)
    if(s1=="five hundred" or s1=="two thousand"):
        classifier=backLoad()
        sleep(2)
        os.system('clear')
        filepath=input("Enter Back Side of Note:")
        label2=currency_classification(classifier,filepath)
        switcher = {
             0 : "five hundred", 
             1: "two thousand",
             2: "invalid image",
        }
        s2=switcher.get(label2, "Not Maching")
        print(s2) 
        if label1==label2:
            print(s1," note detected")
        else:
            print("Invalid note/image")
    else:
        print(s1)

 
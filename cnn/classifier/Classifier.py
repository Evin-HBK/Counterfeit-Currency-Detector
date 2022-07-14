from email.mime import image
import tensorflow as tf
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras import utils
CATEGORIES = ["500","2000"]
import os
from time import sleep
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

def Input(classifier,filepath):
    predict = utils.load_img(filepath, target_size=(224,224))
    predict_modified=utils.img_to_array(predict)
    predict_modified=predict_modified/255
    predict_modified=np.expand_dims(predict_modified,axis=0)
    result= classifier.predict(predict_modified)
    print("filename = "+filepath)
    threshold=0.9

    if result[0][0] >= threshold:
        prediction = '500'
        probability =result[0][0]
        print ("Probability ="+ str(probability))
        print ("Prediction ="+prediction)
        return 500
    elif result[0][0]<=1-threshold:
        prediction= '2000'
        probability = 1 - result[0][0]
        print ("Probability ="+str(probability))
        print("Prediction ="+prediction)
        return 2000
    else:
        prediction='Invalid Image'
        return 0
    print("\n\n")

if __name__=='__main__':
    classifier=frontLoad()
    sleep(2)
    os.system('clear')
    filepath=input("Enter Front Side of Note:")
    value1=Input(classifier,filepath)
    print(str(value1))
    value2=0
    if value1!=0:
        classifier=backLoad()
        sleep(2)
        os.system('clear')
        filepath=input("Enter Back Side of Note:")
        value2=Input(classifier,filepath)
    if value1==value2:
        print("Prediction ="+str(value2))
    else:
        print("Invalid Image")
    exit(0)
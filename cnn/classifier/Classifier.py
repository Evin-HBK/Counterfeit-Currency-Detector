from email.mime import image
import tensorflow as tf
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras import utils
CATEGORIES = ["500","2000"]
import os
from time import sleep
def Load():
    print("Loading Classifier Model ....\n\n")
    classifier = tf.keras.models.load_model("model")
    print("\n\nModel Loaded.\n\n")
    return classifier

def Input(classifier,filepath):
    predict = utils.load_img(filepath, target_size=(150,150))
    predict_modified=utils.img_to_array(predict)
    predict_modified=predict_modified/255
    predict_modified=np.expand_dims(predict_modified,axis=0)
    result= classifier.predict(predict_modified)
    print("filename = "+filepath)
    threshold=0.989

    if result[0][0] >= threshold:
        prediction = '500'
        probability =result[0][0]
        print ("Probability ="+ str(probability))
        print ("Prediction ="+prediction)
    elif result[0][0]<=1-threshold:
        prediction= '2000'
        probability = 1 - result[0][0]
        print ("Probability ="+str(probability))
        print("Prediction ="+prediction)
    else:
        prediction='Invalid Image'
        print("Prediction ="+prediction)
    print("\n\n")

if __name__=='__main__':
    classifier=Load()
    sleep(2)
    os.system('clear')
    files=os.listdir('test_data')
    files.sort()
    for file in files:
        if(file[-3:len(file)]=='jpg' or file[-4:len(file)]=='jpeg' or file[-3:len(file)]=='png'):
            Input(classifier,"test_data/"+file)
    exit(0)
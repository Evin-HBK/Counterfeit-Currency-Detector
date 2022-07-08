from email.mime import image
import tensorflow as tf
import numpy as np
import pandas as pd
from keras.preprocessing.image import ImageDataGenerator
from keras import utils
CATEGORIES = ["500","2000"]
if __name__=='__main__':
    filepath =input("Enter the path:")
    classifier = tf.keras.models.load_model("classifier.model")
    predict = utils.load_img(filepath, target_size=(150,150))
    predict_modified=utils.img_to_array(predict)
    predict_modified=predict_modified/255
    predict_modified=np.expand_dims(predict_modified,axis=0)
    result= classifier.predict(predict_modified)
    if result[0][0] >= 0.8:
        prediction = '500'
        probability =result[0][0]
        print ("Probability ="+ str(probability))
        print ("Prediction ="+prediction)
    elif result[0][0]<=0.2:
        prediction= '2000'
        probability = 1 - result[0][0]
        print ("Probability ="+str(probability))
        print("Prediction ="+prediction)

    else:
        prediction='Invalid Image'
        print("Prediction ="+prediction)


import cv2
import os
import numpy as np

def Blur_Detect(img,filename,threshold):

	# Blur/Shake Detection - Laplacian Operator

	###################################################
	# Experimentally, sharpness > 10 can be accepted  #
	# lap=cv2.Laplacian(img,cv2.CV_64F)				  #
	###################################################
	#norm=np.sqrt(lap**2)
	#sharp=np.average(norm)
	#sharp=np.average(lap)
	#print(filename+' Sharpness = ',sharp)


	###################################################
	# done by calculating varience in laplacian value #
	# produces better results !!					  #
	###################################################
	lap=cv2.Laplacian(img,cv2.CV_64F).var()
	print("\n\n=========================================")
	print(filename+' Sharpness = ',lap)
	if lap>threshold:
		print("Status : Clear Image")
	else:
		print("Status : Blurred Image")
	print("=========================================")


def Brightness_Detect(img,filename,threshold):

	# Image Brightness Calculation

	#########################################################
	# The idea is to convert the image to LAB colorspace 	#
	# The L-channel is the light intensity channel		 	#
	# All the pixel intensities are divided by the 		 	#
	# maximum L value - normalization.					 	#
	# check the mean of the normalized value with threshold #
	# value. 												#
	#########################################################
	L,A,B=cv2.split(cv2.cvtColor(img,cv2.COLOR_BGR2LAB))
	L=np.mean(L/np.max(L))
	print("\n\n=========================================")
	print(filename+' Brightness = ',L)
	if L>threshold:
		print("Status : Bright Image")
	else:
		print("Status : Dark Image")
	print("=========================================")


if __name__=='__main__':

	path=input("Enter the path : ")
	for file in os.listdir(path):
		img=cv2.imread(path+'/'+file,0)

		blur_thrld=1000
		Blur_Detect(img,file,blur_thrld)

		img=cv2.imread(path+'/'+file)
		bright_thrld=200
		Brightness_Detect(img,file,bright_thrld)
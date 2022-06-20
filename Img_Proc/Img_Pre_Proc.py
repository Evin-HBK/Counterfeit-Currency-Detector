import cv2

def Noise_Removal(imgpath):

    # Open Image In Grayscale
    # dst_img=cv2.imread(imgpath,0)
    # (Only good if the input is also grayscale and is platform dependant, for RGB images use cvtColor())       
    src_img=cv2.imread(imgpath)
    Output(src_img,"Original Image")
    dst_img=cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)
    Output(dst_img,"Grayscale Image")

    # Noise Removal - Median Blur Filter (Optimal KSIZE - 3)
    dst_img=cv2.medianBlur(dst_img,3)                               
    Output(dst_img,"Denoised Image")

    # Return original and modified images
    return dst_img,src_img


def Binary_Threshold(img,threshold):

    # Perform binary thresholding on the image to make contour detection easier
    # use trial and error to find out optimal threshold value
    # if not, use adapive mean thresholding or gaussian mean thresholding
    threshold,dst_img=cv2.threshold(img,threshold,255,cv2.THRESH_BINARY)
    Output(dst_img,"Thresholded Image - "+str(threshold))

    return dst_img

def Contour_Detect(src_img,dst_img):

    # Contour detection works well if the image is properly thresholded
    # Here we use the RETR_EXTERNAL or RETR_LIST as we want only the external boundary.
    # Here we use the CHAIN_APPROX_NONE as we need to detect the whole long edge of the note.
    # CHAIN_APPROX_SIMPLE removes the reduntant points and compresses the contour coordinates list, Hence we are not using it.
    contours,hierarchy=cv2.findContours(dst_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    print("Contours")
    print(contours)
    print("\n\nHierarchy")
    print(hierarchy)

    # Next the numpy array containing the coordinates list is passed onto drawContours().
    # This function draws the contour on the image.
    cv2.drawContours(src_img,contours,-1,(0, 255, 0),2,cv2.LINE_4)
    Output(src_img,"Contours Detected Image")

    return contours


def Output(img,title):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__=='__main__':

    #Image Input
    imgpath=input("Enter the path : ")

    #Remove Noise
    dst_img,src_img=Noise_Removal(imgpath)

    #Image Thresholding
    bin_img=Binary_Threshold(dst_img,125)

    #Detect Contours
    contours=Contour_Detect(src_img,bin_img)

    #Display Output
    Output(dst_img,"Final Output")
import cv2
import numpy as np
import copy

def RGB2BW(src_img):
    
    #######################################################################################################
    # Open Image In Grayscale                                                                             #
    # dst_img=cv2.imread(imgpath,0)                                                                       #
    # (Only good if the input is also grayscale and is platform dependant, for RGB images use cvtColor()) #      
    #######################################################################################################

    bw_img=cv2.cvtColor(src_img,cv2.COLOR_BGR2GRAY)
    Output(bw_img,"Grayscale Image")

    return bw_img

def Median_Blur(bw_img,ksize):

    ##########################################################
    # Noise Removal - Median Blur Filter (Optimal KSIZE - 3) #
    # Does not preserve edges as much as bilateral filter    #
    ##########################################################

    blur_img=cv2.medianBlur(bw_img,ksize)                               
    Output(blur_img,"Denoised Image - Median Blur")

    return blur_img

def Bilateral_Blur(bw_img,d,sigmacolor,sigmaspace):

    ###########################################################################
    # Bilateral Blur removes noise in the image but keeps the edges sharpened #
    # Best for edge preserving , helpful for contour detection                #
    # d - diameter of the pixel                                               #
    ###########################################################################

    blur_img=cv2.bilateralFilter(bw_img,d,sigmacolor,sigmaspace)
    Output(blur_img,"Denoised Image - Bilateral Blur")

    return blur_img

def Edge_Sharpen(blur_img):

    ###############################################################################
    # Sharpens the blurred image enhancing the edges even more useful for contour #
    # detection.                                                                  #
    # Using a 3x3 numpy array as parameter for filter2D()                         # 
    ###############################################################################

    filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    shrp_img=cv2.filter2D(blur_img,-1,filter)
    Output(blur_img,"Edge Sharpened Image")

    return shrp_img


def Adpt_Mean_Threshold(shrp_img):

    ##########################################################
    # The first parameter is the size of the matrix used.    #
    # Second parameter is the constant value subtracted from #
    # the gaussian weight calculated from the image.         #
    ##########################################################

    threshold,thr_img=cv2.threshold(shrp_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,11,12)
    Output(thr_img,"Adaptive Mean Thresholded Image - "+str(threshold))

    return thr_img


def Adpt_Gauss_Threshold(shrp_img):


    threshold,thr_img=cv2.threshold(shrp_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,12,12)
    Output(thr_img,"Adaptive Gaussian Thresholded Image - "+str(threshold))

    return thr_img


def Binary_Threshold(shrp_img,threshold):

    ###############################################################################################
    # Perform binary thresholding on the image to make contour detection easier                   #
    # use trial and error to find out optimal threshold value                                     #
    # if not, use adapive mean thresholding or gaussian mean thresholding                         #
    # In global thresholding, we used an arbitrary chosen value as a threshold.                   #
    # In contrast, Otsu's method avoids having to choose a value and determines it automatically. #
    ###############################################################################################

    threshold,thr_img=cv2.threshold(shrp_img,threshold,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    Output(thr_img,"Thresholded Image - "+str(threshold))

    return thr_img

def Contour_Detect(cpy_src_img,dst_img):

    ############################################################################################################################
    # Contour detection works well if the image is properly thresholded                                                        #
    # Here we use the RETR_EXTERNAL or RETR_LIST as we want only the external boundary.                                        #
    # Here we use the CHAIN_APPROX_NONE as we need to detect the whole long edge of the note.                                  #
    # CHAIN_APPROX_SIMPLE removes the reduntant points and compresses the contour coordinates list, Hence we are not using it. #
    ############################################################################################################################

    contours,hierarchy=cv2.findContours(dst_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    #######################################################################################
    # Next the numpy array containing the coordinates list is passed onto drawContours(). #
    # This function draws the contour on the images                                       #
    #######################################################################################

    cv2.drawContours(cpy_src_img,contours,-1,(0, 255, 0),2,cv2.LINE_4)                       
    Output(cpy_src_img,"Initial Contours Detected In Image")

    return contours

def Contour_Approx(contours,src_img):

    #####################################################################################
    # Here we declare two empty lists for storing the epsilon value.                    #
    # The True parameter indicates that the contour to be approximated is closed.       #
    # The variable prec decides the precision of estimation.                            #
    # In each iteration a list of contours is obtained from the list named 'contours'   #
    # and stored in the variable cnt.                                                   #
    # arcLength() finds out the perimeter of the closed shape.                          #
    # approxPolyDP() takes the contour and epsilon value and approximates a polygon     #
    # and stores it contours in approx. approx and epsilon are appended to lists.       #
    # From the epsilon list, polygon with the largest perimeter is obtained and         #
    # cheked if it has 4 sides(rectangle).if yes, boundingRect() function estimates a   #
    # rectangle and cv2.rectangle() draws a rectangle on to the input image.            #
    # x - x coodrinate from origin                                                      #
    # y - y coordinate from origin                                                      #
    # w - width of image                                                                #
    # h - height of image                                                               #
    # the idea is to plot diagonal points                                               #
    # last parameter is the thickness of the marker                                     #
    #####################################################################################

    approxlist=[]
    epsilonlist=[]
    prec=0.03
    for cnt in contours:
        epsilon = prec*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        approxlist.append(approx)
        epsilonlist.append(epsilon)

    rect_index=epsilonlist.index(max(epsilonlist))
    if(len(approxlist[rect_index])==4):

        x,y,w,h = cv2.boundingRect(approxlist[rect_index])
        cv2.rectangle(src_img,(x,y),(x+w,y+h),(255,0,0),3)
        print("Crop Coordinates : ",approxlist[rect_index])
        #cv2.drawContours(src_img,[approxlist[rect_index]],-1,(0, 255, 0),2,cv2.LINE_4)
        Output(src_img,"Approximated Rectangular Contours Detected In Image")

    return x,y,w,h

def Crop(src_img,x,y,w,h):

    ##############################################################################
    # Image is cropped out along the rectangle giving only the image of the note #
    ##############################################################################

    dst_img=src_img[y:y+h,x:x+w]
    Output(dst_img,"Cropped Image")

    return dst_img


def Output(img,title):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__=='__main__':

    ###############
    # Image Input #
    ###############

    imgpath=input("Enter the path : ")
    src_img=cv2.imread(imgpath)
    Output(src_img,"Original Image")


    ###########################
    # Conversion to Grayscale #
    ###########################

    bw_img=RGB2BW(src_img)


    ################
    # Remove Noise #
    ################
    ksize=7
    blur_img=Median_Blur(bw_img,ksize)
    #blur_img=Bilateral_Blur(bw_img,2,1,1)


    ####################
    # Edge Sharpenning #
    ####################

    shrp_img=Edge_Sharpen(blur_img);

    
    ######################
    # Image Thresholding #
    ######################
    
    threshold=137
    thr_img=Binary_Threshold(shrp_img,threshold)
    #thr_img=Adpt_Mean_Threshold(shrp_img)
    #thr_img=Adpt_Gauss_Threshold(shrp_img)


    ###################
    # Detect Contours #
    ###################
    cpy_src_img=copy.deepcopy(src_img)
    contours=Contour_Detect(cpy_src_img,thr_img)
    x,y,w,h=Contour_Approx(contours,cpy_src_img)

    ##############
    # Crop Image #
    ##############

    dst_img=Crop(src_img,x,y,w,h)


    ##################
    # Display Output #
    ##################

    Output(dst_img,"Final Output")
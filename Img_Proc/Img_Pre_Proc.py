import cv2

    def Noise_Removal(imgpath):
        #Image Input
        imgpathpath=input("Enter the path : ")
        src=cv2.imread(imgpath,0)

        #Noise Removal - Median Blur Filter (Optimal KSIZE - 3)
        dst=cv2.medianBlur(src,3)

        #Output
        cv2.imshow("Window1",src)
        cv2.imshow("Window2",dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        cv2.waitKey(1)


    def Resize(imgpath):

if __name__=='__main__':
    Noise_Removal(imgpath)
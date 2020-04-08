#Author - Vignesh
#Github - https://github.com/vicky-ml

#####################
import cv2
import numpy as np

def getTextOverlay(input_image):
    output = np.zeros(input_image.shape, dtype=np.uint8)
   
    #convert the image from BGR to HSV format
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    #Assign threshold values to extract only black text on the image
    lowerthreshold = np.array([0,0,0])
    upperthreshold = np.array([254,255,13])
    #Make only the desired pixels to be visible and mask the rest based on threshold
    masked = cv2.inRange(hsv, lowerthreshold, upperthreshold)
    #AND the masked and original image pixels
    output = cv2.bitwise_not(masked)
    
    #To add gaussianblur to smoothen the pixels abit
    #Comment line19 and uncomment the lines below
    #out = cv2.bitwise_not(masked)
    #blur = cv2.GaussianBlur(out,(5,5),0)
    #output = cv2.addWeighted(blur,2.5,out,-1.5,0)
    
    return output

if __name__ == '__main__':
    image = cv2.imread('simpsons_frame0.png')
    output = getTextOverlay(image)
    cv2.imwrite('simpons_textsmooth.png', output)
    
#####################


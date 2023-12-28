import cv2 #import cv2 library
import imutils #import imutils library
img = cv2. imread("sample2.j jpg") #read an image 
resizeImg = imutils.resize (img, width=20) #resize an Image
cv2. imwrite ("resizedImage jpg" ,resizeImg) #save an image

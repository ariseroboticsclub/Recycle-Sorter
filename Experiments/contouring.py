import imutils
import numpy as np
import cv2
im = cv2.imread('canny_bottleexp.jpg')

#resize the image
ratio = im.shape[0]/100.0
im = imutils.resize(im,height=600)

image =  cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
contours, hierarcy =cv2.findContours(image,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#use -1 as last parameter to use fill color contour, otherwise it's the pixel width of the contour coloring to be drawn on the image
cv2.drawContours(im, contours, -1, (255,255,0),3)
cv2.imshow("contours!!", im)

cv2.waitKey(0)

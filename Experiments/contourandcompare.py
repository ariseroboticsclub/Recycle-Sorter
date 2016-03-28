import imutils
import numpy as np
import cv2
im = cv2.imread('cannyexp.jpg') # a tims cup
im2 = cv2.imread('cannyexp.jpg') # a can 

#resize the image
ratio1 = im.shape[0]/100.0
ratio2 = im2.shape[0]/100.0
im = imutils.resize(im,height=600)
im2 = imutils.resize(im2,height=600)

image1 =  cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
image2 =  cv2.cvtColor(im2,cv2.COLOR_BGR2GRAY)

contours1, hierarcy =cv2.findContours(image1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours2, hierarcy =cv2.findContours(image2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


#use -1 as last parameter to use fill color contour, otherwise it's the pixel width of the contour coloring to be drawn on the image
cv2.drawContours(im, contours1, -1, (255,255,0),3)
#cv2.imshow("contours!!", im1)
cv2.drawContours(im2, contours2, -1, (255,255,0),3)
#cv2.imshow("contours!!", im2)
result =[]
for i in range(len(contours1)):
	result.append(cv2.matchShapes(contours1[i],contours2[i],1,0.0))

print result

import numpy as np
import cv2

im = cv2.imread('capture3.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#im = cv2.drawContours(imgray, contours, -1, (0,255,0), 3)
im = cv2.drawContours(im,contours,-1,(0,255,0),-1)

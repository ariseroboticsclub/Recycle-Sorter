import cv2
import numpy as np
from picamera import PiCamera
import time

camera = PiCamera()
camera.capture('capture6.jpg')

img1 = cv2.imread('timcup.png',0)
img2 = cv2.imread('capture6.jpg',0)

ret, thresh = cv2.threshold(img1, 127, 255,0)
ret, thresh2 = cv2.threshold(img2, 127, 255,0)
contours,hierarchy = cv2.findContours(thresh,2,1)
cnt1 = contours[0]
contours,hierarchy = cv2.findContours(thresh2,2,1)
cnt2 = contours[0]

#print "cnt1 " + str(cnt1)
#print "cnt2 " + str(cnt2)

ret = cv2.matchShapes(cnt1,cnt2,1,0.0)
print ret

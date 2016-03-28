import cv2

image = cv2.imread('can.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_can.jpg', gray_image)
cv2.imshow('color_can', image)
cv2.imshow('gray_can', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

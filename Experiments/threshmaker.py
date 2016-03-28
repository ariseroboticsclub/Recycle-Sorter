import cv2

image = cv2.imread('image2.jpg')
gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image2.jpg', gray_image)

im_gray = cv2.imread('gray_image2.jpg', cv2.CV_LOAD_IMAGE_GRAYSCALE)
(thresh, im_bw) = cv2.threshold(im_gray, 0,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
cv2.imwrite('bw_image3.png', im_bw)

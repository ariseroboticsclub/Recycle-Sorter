import cv2
import numpy as np
from matplotlib import pyplot as plt
<<<<<<< HEAD
img = cv2.imread('gray_image1.jpg', 0)
edges = cv2.Canny(img,50,150)
=======
img = cv2.imread('gray_can.jpg', 0)
edges = cv2.Canny(img,100,200)
>>>>>>> 5e60e653ee9f450bdb97561e5c40d15564e5896c
cv2.imwrite('canny_can.jpg', edges)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title('Original'), plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image'),plt.xticks([]),plt.yticks([])

plt.show()

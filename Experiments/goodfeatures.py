import cv
 
filename =  "burke94.jpg" # replace w/ your filename
grayImage = cv.LoadImage(filename, 2)
eigImage = cv.CreateImage(cv.GetSize(grayImage), cv.IPL_DEPTH_32F, 1)
tempImage = cv.CreateImage(cv.GetSize(grayImage), cv.IPL_DEPTH_32F, 1)
 
cornerMem = []
cornerCount = 300
qualityLevel = 0.1
minDistance = 5
cornerMem = cv.GoodFeaturesToTrack(grayImage, eigImage, tempImage,  cornerCount, qualityLevel, minDistance, None, 3, False)
 
print len(cornerMem), " corners found"
print cornerMem
 
 
for point in cornerMem:
    center = int(point[0]), int(point[1])
    cv.Circle(colorImage, (center), 2, (0,255,255))
cv.SaveImage("savedcolor.jpg",colorImage)
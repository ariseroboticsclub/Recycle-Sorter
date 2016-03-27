#http://opencv-python-tutroals.readthedocs.org/en/latest/py_tutorials/py_feature2d/py_matcher/py_matcher.html
#http://stackoverflow.com/questions/11114349/how-to-visualize-descriptor-matching-using-opencv-module-in-python/14069570#14069570
# matching features of two images
import cv2
import sys
import scipy as sp

if len(sys.argv) < 3:
    print 'usage: %s img1 img2' % sys.argv[0]
    sys.exit(1)

img1_path = sys.argv[1]
img2_path = sys.argv[2]

img1 = cv2.imread(img1_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
img2 = cv2.imread(img2_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)

detector = cv2.FeatureDetector_create("SURF")
descriptor = cv2.DescriptorExtractor_create("BRIEF")
matcher = cv2.DescriptorMatcher_create("BruteForce-Hamming")

# detect keypoints
kp1 = detector.detect(img1)
kp2 = detector.detect(img2)

print '#keypoints in image1: %d, image2: %d' % (len(kp1), len(kp2))

# descriptors
k1, d1 = descriptor.compute(img1, kp1)
k2, d2 = descriptor.compute(img2, kp2)

print '#keypoints in image1: %d, image2: %d' % (len(d1), len(d2))

# match the keypoints
matches = matcher.match(d1, d2)

# visualize the matches
print '#matches:', len(matches)
dist = [m.distance for m in matches]

print 'distance: min: %.3f' % min(dist)
print 'distance: mean: %.3f' % (sum(dist) / len(dist))
print 'distance: max: %.3f' % max(dist)

# threshold: half the mean
thres_dist = (sum(dist) / len(dist)) * 0.5

# keep only the reasonable matches
sel_matches = [m for m in matches if m.distance < thres_dist]

print '#selected matches:', len(sel_matches)

# #####################################
# visualization of the matches
h1, w1 = img1.shape[:2]
h2, w2 = img2.shape[:2]
view = sp.zeros((max(h1, h2), w1 + w2, 3), sp.uint8)
view[:h1, :w1, :] = img1  
view[:h2, w1:, :] = img2
view[:, :, 1] = view[:, :, 0]  
view[:, :, 2] = view[:, :, 0]

for m in sel_matches:
    # draw the keypoints
    # print m.queryIdx, m.trainIdx, m.distance
    color = tuple([sp.random.randint(0, 255) for _ in xrange(3)])
    cv2.line(view, (int(k1[m.queryIdx].pt[0]), int(k1[m.queryIdx].pt[1])) , (int(k2[m.trainIdx].pt[0] + w1), int(k2[m.trainIdx].pt[1])), color)


cv2.imshow("view", view)
cv2.waitKey()
import cv2
from matplotlib import pyplot as plt
image = cv2.imread('download.png',cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([image],[0],None,[256],[0,256])
cv2.imshow('Image', image)
plt.hist(image.ravel(), bins=256, range=(0, 256))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
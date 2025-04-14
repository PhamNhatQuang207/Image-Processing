import matplotlib.image as mpimg
import numpy as np
import matplotlib.pyplot as plt
img = mpimg.imread('download.jpeg')
print('Image dimensions:', img.shape)
def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
gray = rgb2gray(img)
plt.imshow(gray, cmap=plt.get_cmap('gray'))
plt.show()
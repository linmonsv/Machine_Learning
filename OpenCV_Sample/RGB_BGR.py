import matplotlib.pyplot as plt
import numpy as np
import cv2

img = np.array([
    [[255, 0, 0], [0, 255, 0], [0, 0, 255]],
    [[255, 255, 0], [255, 0, 255], [0, 255, 255]],
    [[255, 255, 255], [128, 128, 128], [0, 0, 0]],
], dtype=np.uint8)

plt.imsave('img_pyplot.png', img)

cv2.imwrite('img_cv2.jpg', img)

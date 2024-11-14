import cv2
import numpy as np
import matplotlib.pyplot as plt
# Load the image in grayscale mode
image = cv2.imread('D:/ODDSEM/OSTT/Screenshot.png', 0)
# Plot original image and its histogram
plt.figure(figsize=(12, 5))
# Display Original Image
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Original Image')
plt.axis('off')
# Display Histogram of Original Image
plt.subplot(1, 2, 2)
plt.hist(image.ravel(), 256, [0, 256])
plt.title('Histogram of Original Image')
plt.show()
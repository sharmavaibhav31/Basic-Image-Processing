"""
Inorder to work on this experiment, kindly check the topic “Installing add on Libraries”.
Because we are going to install OpenCV and Pillow in our newly created environment.

Step 1: Install OpenCV and Pillow
Code: !pip install opencv-python Pillow
After successful installation you will see the below details
Installing collected packages: Pillow, numpy, opencv-python
Successfully installed Pillow-10.4.0 numpy-1.24.4 opencv-python-4.10.0.84

Step 2: Install matplotlib
Code: !pip install matplotlib
After successful installation you will see the below details
Installing collected packages: pyparsing, kiwisolver, fonttools, cycler, contourpy, matplotlib
Successfully installed contourpy-1.1.1 cycler-0.12.1 fonttools-4.53.1 kiwisolver-1.4.7 matplot
lib-3.7.5 pyparsing-3.1.4
"""
#--------------------------------------------------------------------------------------------------
#Load and display an image using OpenCV
import cv2
from matplotlib import pyplot as plt
# Load image using OpenCV
image_path = 'images/path/here.jpg/.png/.jpeg.webp' # replace with the path to your image
img = cv2.imread(image_path)
# Convert the image from BGR (OpenCV default) to RGB
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Display the image using matplotlib (since cv2.imshow() doesn't work well in Jupyter)
plt.imshow(img_rgb)
plt.axis('off') # Turn off axis labels
plt.show()

#--------------------------------------------------------------------------------------------------

#Load and display an image using Pillow
from PIL import Image
import matplotlib.pyplot as plt
# Load image using Pillow
image_path = 'images/path/here.jpg/.png/.jpeg.webp' # replace with the path to your image
img_pillow = Image.open(image_path)
# Display the image
plt.imshow(img_pillow)
plt.axis('off') # Turn off axis labels
plt.show()








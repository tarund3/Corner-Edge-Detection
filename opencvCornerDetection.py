import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Assuming your file is in the current directory or a subdirectory
file_name = 'my_image_opencv.jpg'
file_path = os.path.join(current_directory, file_name)
print(f"Full path to the file: {file_path}")

edges = cv2.Canny(image, 100, 200)

lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi/180, threshold=100, minLineLength=50, maxLineGap=10)

image_path = '/content/my_image_opencv.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)

corners = cv2.cornerHarris(image, blockSize=2, ksize=3, k=0.04)

output_image[corners_dilated > 0.01 * corners_dilated.max()] = [0, 0, 255]

plt.figure(figsize=(10,10))
plt.imshow(output_image)
plt.title('Lines and Corners Detection')
plt.show()
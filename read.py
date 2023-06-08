'''
Author: Martin Chow

The script essentially takes an input image, crops and rotates it based on the largest contour, adjusts the orientation if necessary, and
saves the resulting image to the "tmp" directory as "output.png".

    Args:
        input (string): The first input must be file path of the image

    Returns:
        None
'''

try:
    import cv2
    print("cv2 is installed.")
    print("OpenCV version:", cv2.__version__)
except ImportError:
    print("cv2 is not installed.")

import sys
import numpy as np



if len(sys.argv) > 1:
    file = sys.argv[1]
    print("File:", file)
else:
    print("No image file path provided.")

image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

#change the black white image to Binary matrix from 0 to 255(white)
_, thresholded = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)
#Create contours for simple image
contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

largest_contour = max(contours, key=cv2.contourArea)

x, y, w, h = cv2.boundingRect(largest_contour)

cropped_image = image[y:y+h, x:x+w]

epsilon = 0.04 * cv2.arcLength(largest_contour, True)
approx_polygon = cv2.approxPolyDP(largest_contour, epsilon, True)

#get angle with MinAreaRect
rect = cv2.minAreaRect(approx_polygon)
# angle is the last element of the output
angle = rect[2]

height, width = image.shape
#rotated around center
rotation_matrix = cv2.getRotationMatrix2D(( height // 2, width // 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (height, width))

# thresholded, may not require for this problem as it seems like a black white picture, but just added incase
_, thresholded_rotated = cv2.threshold(rotated_image, 127, 255, cv2.THRESH_BINARY)
contours_rotated, _ = cv2.findContours(thresholded_rotated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#crop after rotated
largest_contour_rotated = max(contours_rotated, key=cv2.contourArea)
x_rotated, y_rotated, w_rotated, h_rotated = cv2.boundingRect(largest_contour_rotated)
cropped_image_rotated = rotated_image[y_rotated:y_rotated + h_rotated, x_rotated:x_rotated + w_rotated]

#make sure that the longer dimension is the width and the shorter is the height
height, width = cropped_image_rotated.shape

if(height > width):
    cropped_image_rotated = cv2.rotate(cropped_image_rotated,cv2.ROTATE_90_CLOCKWISE)

#test only
#cv2.imshow("Rotated Image", cropped_image_rotated)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

import os

directory = "tmp"

# Create a new directory if it doesn't exist
if not os.path.exists(directory):
    os.mkdir(directory)
    print("Directory '{}' created.".format(directory))
else:
    print("Directory '{}' already exists.".format(directory))
output_file = "tmp/output.png"


cv2.imwrite(output_file, cropped_image_rotated)
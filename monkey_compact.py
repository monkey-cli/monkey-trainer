import cv2
import os
import subprocess

# File to shrink down the sizes of the captures images
W = 100.

subprocess.run("rm -rf neg", shell=True)
subprocess.run("mkdir neg", shell=True)

subprocess.run("rm -rf pos", shell=True)
subprocess.run("mkdir pos", shell=True)

# resize negatives
for filename in os.listdir('negative'):
    image = cv2.imread('negative/' + filename)
    height, width, depth = image.shape

    imgScale = W / width
    newX, newY = image.shape[1] * imgScale, image.shape[0] * imgScale
    newImage = cv2.resize(image, (int(newX), int(newY)))
    cv2.imwrite("neg/" + filename, newImage)


# resize positives
for filename in os.listdir('positive'):
    image = cv2.imread('positive/' + filename)
    height, width, depth = image.shape

    imgScale = W / width
    newX, newY = image.shape[1] * imgScale, image.shape[0] * imgScale
    newImage = cv2.resize(image, (int(newX), int(newY)))
    cv2.imwrite("pos/" + filename, newImage)

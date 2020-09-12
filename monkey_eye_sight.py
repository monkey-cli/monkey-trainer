import cv2
import numpy as np


# File to test the output cascade generated after trainign.

# default path of cascade
cascadePath = 'output/cascade.xml'
testImagePath = 'test.png'

cascade = cv2.CascadeClassifier(cascadePath)

img = cv2.imread(testImagePath)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detected_objects = cascade.detectMultiScale(gray, 1.3, 5)

print('detected_objects', detected_objects)

for (x, y, w, h) in detected_objects:
    img = cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('output', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import subprocess

imageURI = "test.png"
image = cv2.imread(imageURI)

cv2.imshow("Focus window", image)

while True:
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("EXIT!")
        break
    elif key == ord("p"):
        print("Store positive: ")
        subprocess.run('bash ./monkey-scripts/monkey-screenshot-android.sh positive', shell=True)
    elif key == ord("n"):
        print("Store negative: ")
        subprocess.run('bash ./monkey-scripts/monkey-screenshot-android.sh negative', shell=True)

    
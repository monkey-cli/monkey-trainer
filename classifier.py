import cv2
import subprocess

imageURI = "test.png"
image = cv2.imread(imageURI)

cv2.imshow("Focus window", image)

# Device type, simple check
isIOS = True
scriptPath = None

if isIOS:
    scriptPath = "./monkey-scripts/monkey-screenshot-ios.sh"
else:
    scriptPath = "./monkey-scripts/monkey-screenshot-android.sh"

while True:
    key = cv2.waitKey(1)
    if key == ord("q"):
        print("EXIT!")
        break

    elif key == ord("p"):
        print("Store positive: ")

        subprocess.run('bash %s positive' % (scriptPath), shell=True)
    elif key == ord("n"):
        print("Store negative: ")
        subprocess.run('bash %s negative' % (scriptPath), shell=True)

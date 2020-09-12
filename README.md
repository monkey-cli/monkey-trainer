# monkey-trainer
Cascade Classifier trainer to generate xml classifiers for #monkey-vision


```bash
# Build Dockerfile
docker build .

# Run image detached
docker run -td <image>

# ssh in the running container
docker exec -it <containerID> bash

```


## Training Cascade Classifier

### Step 1
Collect the test data, screenshots.
Run the `classifier.py` scripts for a selected mobile platform `iOS` or `Android` and use the OpenCV modal preview to trigger screenshot capture at a specific time from the running device. (The emulator/simulator must be running)


- Press **"p"** for positive screenshot capture
- Press **"n"** for negative screenshot capture
- Press **"q"** to cancel the capture

### Step 2 
Generate negative description file.
The `.txt` file must contain all the paths of the negative images.
To generate this file run the method `generate_negative_description_file` from `'/cascade.py'`.

### Step 3 
Install `opencv_annotation`, if not installed.
https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html


### Step 4 
Generate positive description file by using `opencv_annotation`.
Run command:

```bash
/path/to/opencv_annotation --annotations=positive.txt --images=positiveDir/

# Example:

/Users/${user}/Desktop/projects/monkey-cli/build_opencv/bin/opencv_annotation --annotations=positive.txt --images=positive/
```
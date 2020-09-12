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
Install `opencv_annotation`, `opencv_createsamples` & `opencv_traincascade`, if not installed.
https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html

```bash
# Steps


git clone https://github.com/opencv/opencv.git

# opencv_createsamples & opencv_traincascade are not part of the latest release
git checkout 3.4

mkdir build_opencv
cd build_opencv

cmake -DCMAKE_BUILD_TYPE=Release ../opencv

make -j7 # runs 7 jobs in parallel
```

### Step 4 
Generate positive description file by using `opencv_annotation`.
Run command:

```bash
/path/to/opencv_annotation --annotations=positive.txt --images=positiveDir/

# Example:

/Users/${user}/Desktop/projects/monkey-cli/build_opencv/bin/opencv_annotation --annotations=positive.txt --images=positive/
```

### Step 5
Create vector file from positives description file.

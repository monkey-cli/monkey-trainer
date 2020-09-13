# monkey-trainer
Cascade Classifier trainer to generate xml classifiers for #monkey-vision


## Training Cascade Classifier

### Step 1
Collect the test data, screenshots.
Run the `classifier.py` scripts for a selected mobile platform `iOS` or `Android` and use the OpenCV modal preview to trigger screenshot capture at a specific time from the running device. (The emulator/simulator must be running)


- Press **"p"** for positive screenshot capture
- Press **"n"** for negative screenshot capture
- Press **"q"** to quit/cancel the capture

### Step 2
Resize collected screenshots. Run the file `monkey_compact.py`. It will resize all the captured images into width 100px and scaled height. After running this script two new folders will be created `/pos` and  `/neg` containing the resized images. **In the following steps is suggested to use the resized images for faster training.**


### Step 3
Generate negative description file.
The `.txt` file must contain all the paths of the negative images.
To generate this file run the method `generate_negative_description_file` from `'/cascade.py'`.

### Step 4 [Optional]
Install `opencv_annotation`, `opencv_createsamples` & `opencv_traincascade`, if not installed.
https://docs.opencv.org/master/d0/db2/tutorial_macos_install.html

```bash
# Steps

git clone https://github.com/opencv/opencv.git

# opencv_createsamples & opencv_traincascade are not part of the latest release/version
# cd into the opencv folder and checkout version 3.4 branch
git checkout 3.4

# cd back to parent dir and create the build directory
mkdir build_opencv
cd build_opencv

cmake -DCMAKE_BUILD_TYPE=Release ../opencv

make -j7 # runs 7 jobs in parallel
```

### Step 5
Generate positive description file by using `opencv_annotation`.
Run command:

```bash
/path/to/opencv_annotation --annotations=positive.txt --images=positiveDir/

# Example:

/Users/${user}/Desktop/projects/monkey-cli/build_opencv/bin/opencv_annotation --annotations=positive.txt --images=positive/
```

### Step 6
Create vector file from positives description file.
Run command:

```bash
/path/to/opencv_createsamples -info positive.txt -w 100 -h 24 -num 1000 -vec positive.vec

# Example
/Users/${user}/Desktop/projects/monkey-cli/build_opencv/bin/opencv_createsamples -info positive.txt -w 100 -h 24 -num 1000 -vec positive.vec
```

### Step 7
Train cascade.
https://docs.opencv.org/master/dc/d88/tutorial_traincascade.html

```bash
/path/to/opencv_traincascade -data output/  -vec positive.vec -bg negative.txt -w 100 -h 24 -numPos 15 -numNeg 100 -numStages 10


# Example:
/Users/${user}/Desktop/projects/monkey-cli/build_opencv/bin/opencv_traincascade -data output/  -vec positive.vec -bg negative.txt -w 100 -h 24 -numPos 15 -numNeg 100 -numStages 10

# - numPos: must be less than the number of the drawn rectangles created in Step 5. 
 
```

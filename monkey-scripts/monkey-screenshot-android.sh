#!/usr/bin/env

# full path
STORAGE_DIR=$1

if [[ ! -n $1 ]]; then
    # screenshots directory not provided
   exit 1
fi

# script variables
TIMESTAMP=`date '+%Y-%m-%d_:_%H-%M-%S'`
SCREENSHOT=/sdcard/$TIMESTAMP._monkey_screenshot.png

# create screenshots directory if it does not exist
mkdir -p $STORAGE_DIR

adb shell screencap -p $SCREENSHOT
adb pull $SCREENSHOT $STORAGE_DIR
adb shell rm $SCREENSHOT

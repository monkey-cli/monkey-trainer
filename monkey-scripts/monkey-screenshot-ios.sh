#!/usr/bin/env

# full path
STORAGE_DIR=$1

if [[ ! -n $1 ]]; then
    # screenshots directory not provided
    exit 1
fi

# script variables
TIMESTAMP=`date '+%Y-%m-%d_:_%H-%M-%S'`

# create screenshots directory if it does not exist
mkdir -p $STORAGE_DIR

SCREENSHOT=$STORAGE_DIR/$TIMESTAMP._monkey_screenshot.png

xcrun simctl io booted screenshot $SCREENSHOT

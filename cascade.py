import os


def generate_negative_description_file():
    # open output file. Will override everything in there if the file existed
    with open('negative.txt', 'w') as f:
        # loop over all images
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')


# call the function
generate_negative_description_file()
import os
import re

# Set the directory path containing the image files to the current script's folder
directory_path = os.path.dirname(os.path.realpath(__file__))

# Regular expression to match and remove numbers within parentheses
regex_pattern = re.compile(r'\s?\([0-9]+\)')

# Iterate through the files in the directory
for filename in os.listdir(directory_path):
    # Check if the file is an image (JPG, PNG, or GIF)
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
        # Remove any number within parentheses from the filename
        new_filename = regex_pattern.sub('', filename)

        # Rename the file if the new filename is different from the original
        if new_filename != filename:
            original_path = os.path.join(directory_path, filename)
            new_path = os.path.join(directory_path, new_filename)
            os.rename(original_path, new_path)
            print(f'Renamed {filename} to {new_filename}')

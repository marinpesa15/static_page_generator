import os
import shutil

def copy_directory_contents(source_dir, destination_dir):

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        destination_item = os.path.join(destination_dir, item)

        if os.path.isdir(source_item):
            copy_directory_contents(source_item, destination_item)
        else:
            shutil.copy(source_item, destination_item)
            print(f"Copied: {source_item} to {destination_item}")
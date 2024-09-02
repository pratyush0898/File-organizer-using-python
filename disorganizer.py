import os
import shutil

def disorganize_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for root, dirs, files in os.walk(source_folder):
        for filename in files:
            source_path = os.path.join(root, filename)
            target_path = os.path.join(destination_folder, filename)

            shutil.move(source_path, target_path)
            print(f"Moved {filename} to {destination_folder}")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    disorganize_files(source_folder, destination_folder)

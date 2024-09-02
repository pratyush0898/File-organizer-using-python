import os
import shutil

def organize_files(source_folder, destination_folder, excluded_extensions):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        if os.path.isfile(source_path):
            file_extension = filename.split('.')[-1].lower()

            if file_extension in excluded_extensions:
                print(f"Ignored {filename}")
                continue

            target_folder = os.path.join(destination_folder, file_extension)

            if not os.path.exists(target_folder):
                os.makedirs(target_folder)

            target_path = os.path.join(target_folder, filename)
            shutil.move(source_path, target_path)
            print(f"Moved {filename} to {target_folder}")

if __name__ == "__main__":
    source_folder = input("Enter the source folder path: ")
    destination_folder = input("Enter the destination folder path: ")

    excluded_extensions = {'.sb3', '.3mf', '.bmp', '.txt', '.mp4', '.ios'}

    organize_files(source_folder, destination_folder, excluded_extensions)

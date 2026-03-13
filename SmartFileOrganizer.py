import os
import shutil

# Folder to organize
source_folder = r"C:\Users\Manasvi\Downloads"
print(f"Organizing files in: {source_folder}")
# File type categories
file_types = {
    "Images": [".jpg", ".png", ".jpeg", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
}
print(os.listdir(source_folder))
# Go through all files
for file in os.listdir(source_folder):

    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):

        for folder, extensions in file_types.items():

            if file.lower().endswith(tuple(extensions)):

                destination_folder = os.path.join(source_folder, folder)

                if not os.path.exists(destination_folder):
                    os.makedirs(destination_folder)

                shutil.move(file_path, os.path.join(destination_folder, file))

                print(f"Moved {file} → {folder}")
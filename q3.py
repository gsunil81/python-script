import os

folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
else:
    print(f"Folder already exists: {folder_name}")
import os

# Walk through the directory tree, including all subdirectories
for root, dirs, files in os.walk('.', topdown=False):
    # Rename files first to avoid conflicts
    for file_name in files:
        if '[ Watermark ]' in file_name:
            new_file_name = file_name.replace(' [ Watermark ]', '')
            os.rename(os.path.join(root, file_name), os.path.join(root, new_file_name))
    
    # Rename directories
    for dir_name in dirs:
        if '[ Watermark ]' in dir_name:
            new_dir_name = dir_name.replace(' [ Watermark ]', '')
            os.rename(os.path.join(root, dir_name), os.path.join(root, new_dir_name))


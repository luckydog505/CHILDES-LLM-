import os

def get_cha_files(folder_path):
    """
    Get all .cha files from the specified folder.
    """
    return [
        os.path.join(folder_path, file)
        for file in os.listdir(folder_path)
        if file.endswith('.cha')
    ]

def log_error(file_path, error):
    """
    Log errors encountered while processing files.
    """
    print(f"Error processing {file_path}: {error}")

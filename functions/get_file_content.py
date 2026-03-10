import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        valid_target_dir = os.path.commonpath([absolute_working_dir, target_path])

        if valid_target_dir != absolute_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(target_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)            
            if f.read(1):
                file_content_string += f'[...File "{target_path}" truncated at {MAX_CHARS} characters]'
            return file_content_string

    except Exception as e:
        return f"Error: {e}"

import os

def write_file(working_directory, file_path, content):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        valid_target_dir = os.path.commonpath([absolute_working_dir, target_path])
        
        if valid_target_dir != absolute_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        if not os.path.isdir(os.path.dirname(target_path)):
            os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        with open(target_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{target_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"
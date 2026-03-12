import os
from google.genai import types

def get_files_info(working_directory, directory="."):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(absolute_working_dir, directory))
        valid_target_dir = os.path.commonpath([absolute_working_dir, target_dir])

        if valid_target_dir != absolute_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        items = os.listdir(path=target_dir)
        result = []

        for item in items:
            target_item = os.path.normpath(os.path.join(target_dir, item))
            item_size = os.path.getsize(target_item)
            item_is_dir = os.path.isdir(target_item)
            item_description = f"- {item}: file_size={item_size} bytes, is_dir={item_is_dir}"
            result.append(item_description)
        return result
    except Exception as e:
        return f"Error: {e}"


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)
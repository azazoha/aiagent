import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(absolute_working_dir, file_path))
        valid_target_dir = os.path.commonpath([absolute_working_dir, target_path])
        if valid_target_dir != absolute_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if file_path[-3:] != ".py":
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_path]
        if args:
            command.extend(args)
        python_result = subprocess.run(command, cwd=absolute_working_dir, capture_output=True, text=True, timeout=30)
        output_str = []

        if python_result.returncode != 0:
            output_str.append(f"Process exited with code {python_result.returncode}")
        if not python_result.stdout and not python_result.stderr:
            output_str.append(f"No output produced")
        if python_result.stdout:
            output_str.append(f"STDOUT:\n{python_result.stdout}")
        if python_result.stderr:
            output_str.append(f"STDERR:\n{python_result.stderr}")
        return "\n".join(output_str)

    except Exception as e:
        return f"Error: executing Python file: {e}"
    

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the working directory and returns its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to run, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                ),
                description="Optional list of arguments to pass to the Python script",
            ),
        },
        required=["file_path"],
    ),
)
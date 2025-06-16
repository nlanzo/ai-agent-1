# get_files_info.py
import os
from pathlib import Path
from google.genai import types


def get_files_info(working_directory, directory=None):
    if directory is None:
        directory = working_directory

    absolute_directory = os.path.abspath(os.path.join(working_directory, directory))
    absolute_working_directory = os.path.abspath(working_directory)

    if not absolute_directory.startswith(absolute_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(absolute_directory):
        return f'Error: "{absolute_directory}" is not a directory'
    
    directory_contents = ""
    for filename in os.listdir(absolute_directory):
        try:
            dir = os.path.join(absolute_directory, filename)
            file_size = os.path.getsize(dir)
            is_dir = os.path.isdir(dir)
        
            directory_contents += f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}\n"
        except Exception as err:
            directory_contents += f"- {filename}: Error: {err}"

    return directory_contents


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
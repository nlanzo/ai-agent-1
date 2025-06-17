import os
from config import MAX_CHARS
from google.genai import types


def get_file_content(working_directory, file_path):
    absolute_directory = os.path.abspath(os.path.join(working_directory, file_path))
    absolute_working_directory = os.path.abspath(working_directory)

    if not absolute_directory.startswith(absolute_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(absolute_directory):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(absolute_directory, 'r') as file:
            str = file.read()
            if len(str) > MAX_CHARS:
                return str[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return str
    except Exception as e:
        return f'Error: Failed to read file "{file_path}": {str(e)}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory."
            ),
        },
        required=["file_path"],
    ),
)
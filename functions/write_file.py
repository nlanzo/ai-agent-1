import os
from google.genai import types


def write_file(working_directory, file_path, content):
    absolute_directory = os.path.abspath(os.path.join(working_directory, file_path))
    absolute_working_directory = os.path.abspath(working_directory)

    if not absolute_directory.startswith(absolute_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(os.path.dirname(absolute_directory)):
        try:
            os.makedirs(os.path.dirname(absolute_directory))
        except Exception as e:
            return f'Error: Failed to create directory "{os.path.dirname(absolute_directory)}": {str(e)}'
    
    try:
        with open(absolute_directory, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f'Error: Failed to write to "{file_path}": {str(e)}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file"
            )
        },
        required=["file_path", "content"],
    ),
)
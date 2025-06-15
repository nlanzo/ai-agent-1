import os
from config import MAX_CHARS


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
    

import os

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

import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    absolute_directory = os.path.abspath(os.path.join(working_directory, file_path))
    absolute_working_directory = os.path.abspath(working_directory)

    if not absolute_directory.startswith(absolute_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(absolute_directory):
        return f'Error: File "{file_path}" not found.'
    
    if not absolute_directory.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file'
    
    try:
        commands = ['python', absolute_directory]
        if args:
            commands.extend(args)
        result = subprocess.run(commands, capture_output=True, text=True, timeout=30, check=True, cwd=absolute_working_directory)
        stdout = result.stdout
        stderr = result.stderr
        return f'Successfully executed "{file_path}"\n\nSTDOUT:\n{stdout}\n\nSTDERR:\n{stderr}'
    except subprocess.TimeoutExpired:
        return f'Error: Execution of "{file_path}" timed out after 30 seconds'
    except subprocess.CalledProcessError as e:
        return f'Process exited with code {e.returncode}\n\nSTDOUT:\n{e.stdout}\n\nSTDERR:\n{e.stderr}'
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
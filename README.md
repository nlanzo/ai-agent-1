# AI Agent Project

An intelligent AI coding agent powered by Google's Gemini 2.0 Flash model that can perform various file system operations and execute Python code. The agent is designed to help with coding tasks by providing automated file management, code execution, and development assistance.

## Features

- **File System Operations**: List directories, read file contents, and write files
- **Code Execution**: Run Python files with optional arguments
- **Intelligent Planning**: AI agent creates function call plans to accomplish user requests
- **Iterative Processing**: Supports multi-step operations with configurable iteration limits
- **Verbose Mode**: Detailed logging for debugging and understanding agent behavior
- **Security**: Restricted to working directory operations for safety

## Architecture

The AI agent uses a function calling approach where:

1. **User Input**: Takes natural language requests from the command line
2. **AI Planning**: Gemini 2.0 Flash analyzes the request and creates a function call plan
3. **Function Execution**: Executes appropriate functions to accomplish the task
4. **Iterative Refinement**: Can perform multiple steps to complete complex requests
5. **Result Delivery**: Returns the final result to the user

## Available Functions

The agent can perform the following operations:

### File System Functions
- **`get_files_info`**: List files and directories in the working directory
- **`get_file_content`**: Read and display file contents
- **`write_file`**: Create or overwrite files with specified content

### Code Execution Functions
- **`run_python_file`**: Execute Python files with optional command-line arguments

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd ai-agent-1
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create a .env file
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

## Usage

### Basic Usage

Run the AI agent with a natural language request:

```bash
python main.py "your request here"
```

### Examples

```bash
# List files in the working directory
python main.py "show me all files in the current directory"

# Read a specific file
python main.py "read the contents of main.py"

# Run a Python file
python main.py "run the calculator app with expression '3 + 5'"

# Create a new file
python main.py "create a new file called test.py with a hello world function"

# Complex multi-step operations
python main.py "read the calculator code, then run it with the expression '10 * 5'"
```

### Verbose Mode

Enable detailed logging to see the agent's decision-making process:

```bash
python main.py --verbose "your request here"
```

This will show:
- Function calls being made
- Token usage statistics
- Function responses
- Iteration details

## Configuration

Edit `config.py` to customize the agent's behavior:

```python
MAX_CHARS = 10000          # Maximum characters for file operations
WORKING_DIRECTORY = "./calculator"  # Default working directory
MAX_ITERATIONS = 20        # Maximum iterations for complex tasks
```

## Project Structure

```
ai-agent-1/
├── main.py                 # Main application entry point
├── config.py              # Configuration settings
├── prompts.py             # System prompt for the AI agent
├── requirements.txt       # Python dependencies
├── functions/             # Function implementations
│   ├── call_function.py   # Function calling orchestrator
│   ├── get_file_content.py # File reading functionality
│   ├── get_files_info.py  # Directory listing functionality
│   ├── run_python_file.py # Python file execution
│   └── write_file.py      # File writing functionality
├── calculator/            # Example project for testing
│   ├── main.py           # Calculator application
│   ├── pkg/              # Calculator package
│   └── README.md         # Calculator documentation
└── tests.py              # Test suite
```

## Security Considerations

- **Working Directory Restriction**: The agent is restricted to operations within the configured working directory
- **No Network Access**: Functions are limited to local file system operations
- **Input Validation**: All function inputs are validated before execution
- **Error Handling**: Comprehensive error handling prevents system issues

## Dependencies

- **google-genai**: Google's Gemini AI API client
- **python-dotenv**: Environment variable management

## API Key Setup

1. Get a Gemini API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Add it to your `.env` file:
```
GEMINI_API_KEY=your_actual_api_key_here
```

### Project from boot.dev
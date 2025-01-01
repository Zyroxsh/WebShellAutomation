# Web Shell Automatic Tool

This script is designed to automate the process of exploiting a web shell vulnerability on a target URL. It allows users to check if a target is vulnerable, execute commands, and create a non-interactive shell session.

## Modules
- **sys**: Provides access to some variables used or maintained by the interpreter.
- **time**: Provides various time-related functions.
- **argparse**: Provides a command-line argument parsing functionality.
- **requests**: Allows you to send HTTP requests.

## Color Codes
- **purple, cyan, darkCyan, blue, green, yellow, red, bold, underline, end**: ANSI escape sequences for colored terminal output.

## Banner
- A stylized banner displayed at the start of the script.

## Argument Parser
Initializes the argument parser and defines the following arguments:
- `-u`, `--url`: URL of the target (e.g., http://example.com/shell.php)
- `-p`, `--parameter`: Parameter to use (without the '?=')
- `-c`, `--command`: Command to be executed
- `-s`, `--shell`: Create a non-interactive shell instead of executing a unique command (default: False)

## Functions

### `check_vulnerability(url, parameter)`
Checks if the target URL is vulnerable by sending a request with a 'whoami' command.
- **Args**:
    - `url` (str): The target URL.
    - `parameter` (str): The parameter to use.
- **Returns**:
    - `bool`: True if the target is vulnerable, False otherwise.

### `execute_command(url, parameter, command)`
Executes a command on the target URL.
- **Args**:
    - `url` (str): The target URL.
    - `parameter` (str): The parameter to use.
    - `command` (str): The command to execute.
- **Prints**:
    - The output of the executed command.

## Main Function

### `main(args)`
The main function that orchestrates the script's execution.
- **Args**:
    - `args` (Namespace): Parsed command-line arguments.
- **Prints**:
    - Various status messages and handles the script's logic flow.

## Execution
- The script starts execution from the main block, which calls the main function with parsed arguments.
- Handles exceptions and keyboard interrupts gracefully.

"""Main application script for generating a greeting file."""

import os
from datetime import datetime

# Please customize the following variables
USER_NAME = "ethanwchen"
VERSION = "1.0.0"
DEFAULT_DIR = "/app/data/"

def say_hi(msg: str = "Hello from CI/CD deployment!") -> None:
    """Creates a file with a greeting message."""
    # Generate timestamp
    timestamp = datetime.now().strftime("%Y%m%d%H%M")

    # Ensure the directory exists
    os.makedirs(DEFAULT_DIR, exist_ok=True)

    # Define filename with timestamp
    file_name = f"outputfile_{USER_NAME}_{VERSION}_{timestamp}.txt"
    file_path = os.path.join(DEFAULT_DIR, file_name)

    # Write message to the file
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(msg)

    print(f"File '{file_path}' created successfully.")

def add_numbers(first_number: int, second_number: int) -> int:
    """Returns the sum of two numbers."""
    return first_number + second_number

if __name__ == "__main__":
    say_hi()

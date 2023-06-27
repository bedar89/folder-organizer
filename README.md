# Folder-organizer

## Overview
This script automates the creation of folders based on a defined folder structure specified in a YAML file. It creates folders recursively, adds a README.md file with the folder's title and description, and supports optional parameters for customizing the output location.

## Features
- Creates folders according to a defined folder structure
- Supports recursive folder creation
- Adds a README.md file with the title and description to each folder
- Optional test parameter to create folders in a unique subfolder
- Customizable target location parameter

## Getting Started
To use this script, follow the instructions below:

### Prerequisites
- Python 3 installed on your system
- YAML library (`pyyaml`) installed (you can install it using `pip install pyyaml`)

### Installation
1. Clone the repository or download the script file (`make.py`) to your local machine.

### Usage
1. Prepare a YAML file (`structure.yaml`) to define the folder structure. See the provided example file for reference.

2. Open a terminal or command prompt.

3. Navigate to the directory where the `make.py` script is located.

4. Run the script with the following command:
   ```bash
   python3 make.py [target_directory]
   ```
   - If you provide the `target_directory` parameter, the folders will be created in the specified location. If the parameter is not provided, the folders will be created in the current directory.
   - To create the folders in a unique subfolder (for testing purposes), use the `test` parameter:
     ```bash
     python3 make.py test
     ```

## FAQ

### Q: How can I modify the folder structure?
A: To modify the folder structure, open the `structure.yaml` file and update it according to your requirements. The structure follows a hierarchical format using YAML syntax.

### Q: Can I customize the output location?
A: Yes, you can specify the target directory where the folders will be created by providing it as a parameter when running the script. If no parameter is provided, the script will create the folders in the current directory.

### Q: How can I test the folder creation without affecting my current directory?
A: You can use the `test` parameter when running the script. This will create a unique subfolder and create the folders inside it, allowing you to test the functionality without modifying your current directory.

### Q: How can I contribute to this project?
A: If you'd like to contribute to this project, you can fork the repository, make your desired changes, and submit a pull request. Your contributions are highly appreciated!

## License
This project is licensed under the [MIT License](LICENSE).

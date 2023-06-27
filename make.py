import os
import sys
import yaml


def create_folders(folder, description, subfolders):
    # Create the folder if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)

        # Create the README.md file inside the folder
        readme_title = os.path.basename(folder)
        with open(f"{folder}/README.md", "w") as readme_file:
            readme_file.write(f"# {readme_title}\n\n{description}\n")

    # Iterate over subfolders
    for subfolder in subfolders:
        subfolder_name = subfolder.get("name")
        subfolder_description = subfolder.get("description")
        subfolder_folders = subfolder.get("folders", [])

        # Call create_folders recursively for each subfolder
        create_folders(os.path.join(folder, subfolder_name), subfolder_description, subfolder_folders)


def generate_folders(yaml_file, output_dir):
    with open(yaml_file, "r") as file:
        folders = yaml.safe_load(file)

    create_folders(output_dir, "", folders)


def generate_test_subfolder():
    import time
    timestamp = time.strftime("%Y%m%d%H%M%S")
    return f"test_{timestamp}"


# Main script
yaml_file = "structure.yaml"

# Check if the structure.yaml file exists
if not os.path.isfile(yaml_file):
    print("Error: structure.yaml file not found.")
    sys.exit(1)

# Check if the script is called with 'test' parameter
if len(sys.argv) > 1 and sys.argv[1] == "test":
    subfolder_name = generate_test_subfolder()
    output_dir = f"./{subfolder_name}"
elif len(sys.argv) > 1:
    output_dir = sys.argv[1]
else:
    output_dir = "."

# Generate the folders from structure.yaml
generate_folders(yaml_file, output_dir)

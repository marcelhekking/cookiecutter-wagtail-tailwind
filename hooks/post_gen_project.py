import os

# Define the path to the file where the original working directory is stored
original_working_directory_file = "original_working_directory.txt"

# Read the original working directory from the file
with open(original_working_directory_file, "r") as file:
    original_working_directory = file.read().strip()

# Print the original working directory to verify
print(f"Original working directory: {original_working_directory}")

# Define the path to the template file where you want to insert the original working directory
template_file_path = original_working_directory + "/.env_var"

# Check if the file exists
if os.path.exists(template_file_path):
    # Read the file content
    with open(template_file_path, "r") as file:
        content = file.read()

    # Insert the original working directory into the file
    content = content.replace("current_working_dir", original_working_directory)

    # Write the modified content back to the file
    with open(template_file_path, "w") as file:
        file.write(content)

    print(f"Inserted the original working directory into {template_file_path}")
else:
    print(f"Error: File {template_file_path} does not exist.")

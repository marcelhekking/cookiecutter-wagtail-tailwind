from pathlib import Path

current_working_directory = Path.cwd().resolve()
file_path = ".env_var"


with open(file_path, "r") as file:
    content = file.read()

content = content.replace(
    "current_working_dir",
    str(current_working_directory)
)

with open(file_path, "w") as file:
    file.write(content)

print(f"Inserted the current working directory into {file_path}")
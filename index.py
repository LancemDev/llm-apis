import subprocess
import os

def add_space_to_file(file_path):
    # Open in append mode, which creates the file if it doesn't exist
    with open(file_path, 'a') as file:
        file.write(' ')   # Add a space at the end

def commit_and_push(directory, message, specific_file):
    # Add a space at the end of the specific file
    specific_file_path = os.path.join(directory, specific_file)
    add_space_to_file(specific_file_path)
    
    # Change to the specified directory
    os.chdir(directory)
    
    # Add, commit, and push changes
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])

    print(f"Pushed changes to {directory} with message: {message}")

# Usage
directory_path = "C:\\Users\\Lance\\Desktop\\CODEWRLD\\mksu-examflow"
specific_file = "example.txt"  # Specify the file you want to add a space to
commit_message = "Update API routes with space at the end of example.txt"
commit_and_push(directory_path, commit_message, specific_file)

for i in range(10):
    # Usage
    directory_path = "C:\\Users\\Lance\\Desktop\\CODEWRLD\\mksu-examflow"
    specific_file = "example.txt"  # Specify the file you want to add a space to
    commit_message = "Update API routes with space at the end of example.txt"
    commit_and_push(directory_path, commit_message, specific_file)
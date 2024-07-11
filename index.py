import subprocess
import os

def commit_and_push(directory, message):
    os.chdir(directory)
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", message])
    subprocess.run(["git", "push"])

    print(f"Pushed changes to {directory} with message: {message}")


directory_path = "C:\\Users\\Lance\\Desktop\\CODEWRLD\\mksu-examflow"
commit_message = "Update API routes"
commit_and_push(directory_path, commit_message)
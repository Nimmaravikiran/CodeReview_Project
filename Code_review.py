import subprocess
import re


def run_shell_command(command):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()


def check_pep8(file_path):
    print("Checking PEP 8 compliance...")
    result = run_shell_command(f"pep8 {file_path}")
    if result:
        print(f"PEP 8 issues found:\n{result}")
    else:
        print("PEP 8 check passed.")


def check_docstring(file_content):
    print("Checking docstrings...")
    if not re.search(r'""".*?"""', file_content, re.DOTALL):
        print("No docstring found.")


def check_todo_comments(file_content):
    print("Checking for TODO comments...")
    if re.search(r'\bTODO\b', file_content):
        print("TODO comments found. Please address them.")


def code_review(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()

    check_pep8(file_path)
    check_docstring(file_content)
    check_todo_comments(file_content)


if __name__ == "__main__":
    file_path = r'C:\Users\Ravikiran\PycharmProjects\django_getting-started\CodeAlpha\hangman_game.py'
    code_review(file_path)

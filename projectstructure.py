import os
from pathlib import Path

while True:
    project_name = input("Enter the Src project name: ").strip()
    if project_name:
        break  # Ensures user doesn't enter an empty name

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{project_name}/__init__.py",
    f"{project_name}/components/data_ingestion.py",
    f"{project_name}/components/data_preprocessing.py",
    f"{project_name}/components/model_loading.py",
    f"{project_name}/components/model_evaluation.py",
    f"{project_name}/pipeline/inference.py",
    f"{project_name}/pipeline/training.py",
    f"{project_name}/exception.py",
    f"{project_name}/logger.py",
    "templates/index.html",
    "statics/style.css",
    "notebook/research.ipynb",
    "init_setup.sh",
    "requirements.txt",
    "Dockerfile",
    "app.py",
    "setup.py",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir = filepath.parent  # Get directory part

    if filedir:
        os.makedirs(filedir, exist_ok=True)  # Create directory if it doesn’t exist

    if not filepath.exists():  # Ensures file doesn't already exist
        filepath.touch()  # Create an empty file

print("Project structure created successfully!")

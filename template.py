import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "holiday_management"

list_of_files = [
    #Config
    f"{project_name}/config/__init__.py",
    f"{project_name}/config/settings.py",

    #Agents
    f"{project_name}/agents/__init__.py",
    f"{project_name}/agents/planner_agent.py",
    f"{project_name}/agents/researcher_agent.py",

    #Teams
    f"{project_name}/teams/__init__.py",
    f"{project_name}/teams/holliday_team.py",

    #Utils
    f"{project_name}/utils/__init__.py",
    f"{project_name}/utils/utils.py",

    #Root files inside the project
    "app.py"
]

for file_path in list_of_files:
    filepath = Path(file_path)
    filedir, filename = os.path.split(filepath)

    # Only create the directory if the path actually contains folders
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        with open(filepath, 'w') as f:
            f.write("File is created..")  # Create an empty file 
            pass
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")
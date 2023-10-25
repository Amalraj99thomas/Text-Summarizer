import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:,')

project_name = "textsummarizer"

file_list = [
    ".github/workflows/.gitkeep",
    f" src/{project_name}/__init__.py",             #constructor file
    f"src/{project_name}/conponents/__init__.py",   
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",          #
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",

]


for filepath in file_list:
    filepath = Path(filepath)    #for / path error
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok = True)
        logging.info(f"Created directory: {filedir} for the file: {filename}")


    if(not os.path.exists(filepath)) or (not os.path.getsize(filepath) == 0):       #if size is not 0, there could be code inside the file
        with open(filepath, "w") as f:
            pass
            logging.info(f"Created empty file: {filepath}")


    else:
         logging.info(f"{filepath} already exists!")


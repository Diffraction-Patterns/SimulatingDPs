# How to setup your environment

## Prerequisite 
Ensure Python is installed on your device. Recommended to [install](https://www.python.org/downloads/) the version before the latest version.

## Virtual Environment
We will be using a virtual environment to ensure independency and isolation. As package usage grows, so does bloat. Use of a virtual environment ensures our base project remains clean and reproducible.

A virtual environment is essentially a copy of the Python interpreter that will contain all the packages required for the project.

In the project root, invoke the [venv](https://docs.python.org/3/library/venv.html) command in the terminal. (You can name the virtual environment anything. Typically, it will be called ".venv")

### Commands
```bash
# Create a virtual environment 
# (Windows)
py -m venv .venv

# (macOS & Linux)
python3 -m venv .venv

# Activate the virtual environment
# (Windows)
.venv\Scripts\activate

# (macOS & Linux)
source ./.venv/bin/activate

# Activation can be seen in the command line path
(.venv)

# Deactivate by typing in the command line interface (CLI).
deactivate
```
*While developing, you should have the virtual environment active!

## Packages
To ensure the project is set up with the correct dependencies, we will use a _requirements.txt_ file.

The _requirements.txt_ file contains a list of packages or libraries needed for a project. It ensures a consistent environment.

### Commands
```bash
# With your venv active and in the root directory of your project

# Create/Update requirements.txt
pip freeze > requirements.txt

# Installation
pip install -r requirements.txt
```

## Running the project
To run the program, our entry point will be in the src\simulation directory (our Python package)

```bash
# Ensure your virtual env is active
.venv\Scripts\activate

# Run the command to install packages in editable mode
pip install -e .

# In the root directory, run the command:
python -m simulation
```

## Developing
To maintain a modular and clean project, development should take place in separate packages (if possible).

To complete a new Python package:
1. Create a new folder within the _src_ directory.
2. Create a new ```python __init__.py ``` file to denote the directory as a Python package. 
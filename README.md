# Drishti Microservice

A microservice just to generate graphical report.

## Commands to set Up the project

- Generate the python virtual environment - python -m venv env
- Activate the environment
    1. For Windows Powershell - .\env\Scripts\Activate.ps1
    2. For Windows Bash - source ./env/Scripts/activate
    3. For Mac, Linux - source ./env/bin/activate
- Check whether it is working
    1. For Windows Powershell - Get-Command pip
    2. For Mac, Linux, Windows Bash - which pip
- Upgrade to latest pip version on your local environment - python -m pip install --upgrade pip
- install requirements - pip install -r requirements.txt
- Run the application - uvicorn main:app --reload
- All the apis will be visible at "/docs" route
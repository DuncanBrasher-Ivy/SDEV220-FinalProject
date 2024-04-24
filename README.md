# IvyMesh - A clone of [Canvas](https://www.instructure.com/) for [Ivy Tech](https://www.ivytech.edu/)



# Development
These are the basic steps to set up a local development environment for IvyMesh:


1. Clone this repository

    ```
    git clone https://github.com/DuncanBrasher-Ivy/SDEV220-FinalProject
    cd SDEV220-FinalProject
    ```

2. Create a Python virtual environment

    ```
    python3 -m venv .venv
    ```


3. Activate the virtual environment

    - Bash

        ```
        source .venv/bin/activate
        ```

    - Powershell

        ```
        source .venv/bin/activate.ps1
        ```

    - Fish

        ```
        source .venv/bin/activate.fish
        ```


4. Download dependencies

    ```
    pip3 install -r requirements.txt
    ```


# Deployment
## Python Anywhere
These are the basic steps to deploy to [https://pythonanywhere.com](https://pythonanywhere.com):


1. Create a Bash shell on the Python Anywhere website
2. Run the following command:

    ```
    pa_autoconfigure_django.py https://github.com/DuncanBrasher-Ivy/SDEV220-FinalProject.git --branch=main
    ```



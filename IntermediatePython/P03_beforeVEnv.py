print(
    """
A virtual environment (venv) is a space where you can work an exclusive python 
version/space with its own modules that if you update, it won't affect 
your local computer versions.
Let's use it:
FOR DEBIAN OR UBUNTU:
    * Prerrequistes/Installation: 'sudo apt install python3-env' or 
      'sudo apt install python3.8-venv'
    * Initialize Venv: 'python3 -m venv venv'
    * Activate Venv: 'source venv/bin/activate'
FOR WINDOWS: 
    * Make sure you have installed python3 with venv
    * Initialize Venv: 'py -m venv venv'
    * Activate Venv: '.\\venv\Scripts\\activate'

Now, we need to install package, these expand the use of python in many ways,
 like implementing managment of data, matrix operations or even IA:
PIP: Package Installer for Python
    * Use it only inside the venv, if you it is used in only one project.
    - 'pip freeze' --> Display the avialable modules
    - 'pip install pandas' --> Install the pandas module.
    - 'pip freeze > requirements.txt --> Export dependencies.

FINAL NOTES:
    - The next lessons would be in the "LessonsInVenv" directory, you will not
    see the venv/ directory here as it is specified to be ignored in 
    the .gitignore, you should try and create a Venv for use them, the first
    initial dependency is 'Python-3.8', others will be specified later.
"""
)

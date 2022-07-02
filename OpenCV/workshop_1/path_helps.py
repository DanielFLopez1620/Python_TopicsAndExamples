"""
Author: Daniel Lopez
"""

import os


def get_path(file_name):
    """
    Obtain all the path linked to the file, relative to workshop.
    This works when you are opening the file with VS Code from the path of
    the git clone, in this case, 'Python_TopicsAndExamples'.

    file_name --> NAme of the file you want to access (read/write)

    return file_path --> The complete path from 'Python_TopicsAndExamples'
    """
    file_path = os.getcwd()
    file_path = os.path.join(file_path, "OpenCV")
    file_path = os.path.join(file_path, "workshop_1")
    file_path = os.path.join(file_path, file_name)
    return file_path


def get_path(file_name, additional_dir):
    """
    Obtain all the path linked to the file, relative to workshop.
    This works when you are opening the file with VS Code from the path of
    the git clone, in this case, 'Python_TopicsAndExamples'.

    file_name --> Name of the file you want to access (read/write).
    additional_dir --> Includes the specific directory from the file.

    return file_path --> The complete path from 'Python_TopicsAndExamples'
    """
    file_path = os.getcwd()
    file_path = os.path.join(file_path, "OpenCV")
    file_path = os.path.join(file_path, "workshop_1")
    file_path = os.path.join(file_path, additional_dir)
    file_path = os.path.join(file_path, file_name)
    return file_path

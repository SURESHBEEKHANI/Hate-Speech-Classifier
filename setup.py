from setuptools import find_packages, setup
from typing import List

# Define a constant for an editable install option '-e .' 
# (used in Python to install the package in editable mode, which is often needed for development purposes)
EDITABLE_INSTALL = '-e .'

def parse_requirements(file_path: str) -> List[str]:
    """
    This function reads the requirements file and collects a list of packages needed for the project.
    It ignores any lines that include the editable install option '-e .'.
    """
    with open(file_path, 'r') as file:
        # Read each line, clean it up by removing extra spaces, and exclude '-e .' if found
        requirements = [line.strip() for line in file if line.strip() and line.strip() != EDITABLE_INSTALL]
    return requirements  # Return the list of necessary packages

# Now we set up the project with the following details:
setup(
    name="hate-speech-classification",  # Name of the project
    version="1.0.0",  # Version number of the project
    packages=find_packages(),  # Automatically find and include all packages in this project folder

    # Information about the author (the person who made this project)
    author="Suresh Beekhani",
    author_email="sureshbeekhani26@gmail.com",

    # Short description about the project
    description="A tool for classifying hate speech using machine learning.",
    
    # Long description of the project, giving more details on what it does
    long_description="This package provides models and tools to identify and classify hate speech using natural language processing techniques.",
    long_description_content_type="text/markdown",  # The format for the long description

    # Link to the project's GitHub repository
    url="https://github.com/SURESHBEEKHANI/Hate-Speech-Classifier.git",
    
    # This part reads from requirements.txt, which lists all necessary packages 
    install_requires=parse_requirements('requirements.txt'),

    # Licensing and classification info (optional metadata for others to understand and categorize the project)
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

from setuptools import setup, find_packages
# read the contents of README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name='KDTree4RRT',
    version='0.0.1',
    description='A KDTree Implementation meant for use with the Rapidly Exploring Random Tree Algorithm',
    author='Ofek Peres',
    url="https://github.com/OfekPeres/KDTree4RRT",
    packages=find_packages(),
    install_requires=[
        'typing',
        'numpy',
        'matplotlib'
    ],
)

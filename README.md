# OCR_DAP_10
Développeur d'Application Python - Projet 10



## Setup

### Directory setup
It is recommended to create a dedicated directory to download the project.
In a terminal:
`mkdir dir_name`

### Git setup
Initialize your local Git repository. In a terminal (in your dedicated directory):
`git init`

Then clone the remote repository in your local repository with the https link. You will find the https link is in the "code" drop-down menu:
`git clone https://github.com/clementboloch/OCR_P10.git`

### Virtual environment setup
Install pipenv if you haven't already. You can install it using pip:
`pip install pipenv`
Go inside the `OCR_P10` directory and initialize a new virtual environment using pipenv before installing the dependencies:
`cd OCR_P9`
`pipenv --python 3.9`

Install the required packages from the Pipfile:
`pipenv install`

And activate the virtual environment:
`pipenv shell`


## Launch the program

Go inside the `src` directory and launch the local server:
`cd src`
`python manage.py runserver`

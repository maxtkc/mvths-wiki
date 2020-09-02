# Setting Up Virtual Environment For Python

## Overview

Before writing your first code file, you should learn how to create a virtual environment for Python. Python virtual environment is a self-contained directory tree that includes a Python installation and number of additional packages.

The main purpose of Python virtual environments is to create an isolated environment for different Python projects. This way you can install a specific version of a module on a per project basis without worrying that it will affect your other Python projects.

# Install Venv

Use the command below to install the python3-venv package that provides the venv module which will allow you to create a virtual environment.

#### $ sudo apt install python3-venv

# Create Environment

Switch to the directory where you would like to store your Python 3 virtual environments. Within the directory run the following command to create your new virtual environment:

#### $ python3 -m venv my-project-env

The command above creates a directory called my-project-env, which contains a copy of the Python binary, the Pip package manager, the standard Python library and other supporting files.

To start using this virtual environment, you need to activate it by running the activate script:

#### $ source my-project-env/bin/activate

Once activated, the virtual environment’s bin directory will be added at the beginning of the $PATH variable. Also your shell’s prompt will change and it will show the name of the virtual environment you’re currently using as in the following example.

#### (my-project-env) $

Now that the virtual environment is activated, you can start installing, upgrading, and removing packages using pip. Once you are done with your work to deactivate the environment, simply type deactivate and you will return to your normal shell.

#### (my-project-env) $ deactivate

VIM PYTHON SPACE CONVERSION

# Overview

It is sometimes helpful to be able to quickly convert a large python file that uses spaces to tabs. Best to do the following with list set so you can see all the punctuation marks.

#### :set tabstop=2 " To match the sample file

#### :set noexpandtab " Use tabs, not spaces

#### :%retab\! " Retabulate the whole file

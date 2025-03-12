# First time setup

## Automated
1. give read write permissions to setup.sh ```chmod u+x setup.sh```
2. run the script: ```./setup.sh```
3. done :)

## Manual 
1. setup python virtual environment(venv), run: ```python3 -m .venv```
2. activate venv by running: ```source .venv/bin/activate```
3. verify venv is active: ```which python3```
    output should look like: ```path/to/server/.venv/bin/python3```
4. install pip: ```python3 -m pip install --upgrade pip```
5. install all dependencies from requirements.txt: ```pip install <package-name-from-requirements.txt>```


Note:
    every time a new package is installed, such as running ```pip install <package-name>```
    the environment needs to be activated again.


# Development

## Running the app

documentation for [fastapi](https://fastapi.tiangolo.com/tutorial/first-steps/)
1. run ```fastapi main.py``` to get started

## Running the tests

Ommits print statement outputs
1. run ```pytest``` from within server 

To view prints include the -s flag

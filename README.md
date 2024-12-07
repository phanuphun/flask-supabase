# My Flask Notes 

## Flask Setup Project
1. Create virtual environment in python with `python -m venv env`
2. access to env with `env/Scripts/activate`
3. install Flask `pip install flask`
4. set our .py python to flask know where to run file with `set FLASK_APP=<filename>`

## How to run 
1. access to enn first
2. Run `flask run` for run http://127.0.0.1:5000 , this is a default of Flask.
   - you can defind specific host or port like this `flask run --host=<ip> --port=<portNumber>`
   - you can use `--debug` for debug mode when your code changed
3. If you are aready setup app instant of flask in your file, you can run `pythom <filename>` insteard.

## Basic Command
1. Create requirements.txt with `pip freeze > requirement.txt`
2. install dependencies following requirements.txt with `pip install`

## VSCode Extention 
- [flask-snippets](https://marketplace.visualstudio.com/items?itemName=cstrap.flask-snippets)
# Flask Sample Web API with Supabase
this project created to practice using python building Restful API and try to use supabase 

## Setup and Installation 
- Create `.env` file ypur root directory , Then set environment variables 
  - Note : This project does not use RLS. if you want to use it for auth , you can config supabase connection in `/app/config/supabase_client.py`)
```shell
SUPABASE_URL = '---YOUR_SUPABASE_URL---'
SUPABASE_KEY = '---YOUR_SUPABASE_API_KEY---'
```
- Run `python -m venv env` to create a virtual environment
- Run `env/Scripts/activate` for activate to virtual environment 
- Run `pip install -r requirements.txt` for install dependencies following requirements.txt
- Run `python main.py` to start api on `http://localhost:5000`
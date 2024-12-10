from flask import Flask , request , jsonify
from app.config.supabase_client import supabase
from dotenv import load_dotenv
import os
import sys
import pprint

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# App registration
from app.router.books_route import books_route
from app.router.categories_route import categories_route
from app.router.login_route import login_route
app = Flask(__name__)
app.register_blueprint(books_route)
app.register_blueprint(categories_route)
app.register_blueprint(login_route)

if __name__ == '__main__' :
    app.run(debug=True)
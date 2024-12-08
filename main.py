from flask import Flask , request
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# App registration
from app.router.books_route import books_route
from app.router.categories_route import categories_route
app = Flask(__name__)
app.register_blueprint(books_route)
app.register_blueprint(categories_route)

if __name__ == '__main__' :
    app.run(debug=True)
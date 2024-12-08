from flask import Flask , request
from supabase import create_client, Client
from dotenv import load_dotenv
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

load_dotenv()

# supabase connect
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Check database connection
try:
    response = supabase.table('books').select('*').execute()
    print("Supabase Connected !!!")
except Exception as e:
    print("Error connecting to Supabase:")
    print(e)

# App registration
from app.routes.books_routes import site_route
app = Flask(__name__)
app.register_blueprint(site_route)


if __name__ == '__main__' :
    app.run(debug=True)
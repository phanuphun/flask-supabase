from supabase import create_client, Client
import os
from dotenv import load_dotenv

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
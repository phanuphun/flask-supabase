from flask import Flask 
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__)

# App registration
from app.router.index_routes import registration_routes
registration_routes(app)

if __name__ == '__main__' :
    app.run(debug=True)
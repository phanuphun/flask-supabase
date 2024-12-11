import jwt
import os
from dotenv import load_dotenv
from app.utils.date import jwt_exp

load_dotenv()

key = os.getenv('PRIVATE_KEY')
alg = 'HS256'

def create_token(payload,remember:bool):
    exp = jwt_exp(remember)
    data = {
        'user_data' : payload,
        'exp' : exp
    }
    return jwt.encode(data, key, algorithm=alg)

def token_validate(token):
    try:
        decoded_data = jwt.decode(token, key, algorithms=[alg])
        return {"valid": True, "data": decoded_data}

    except jwt.ExpiredSignatureError:
        # token expire
        return {"valid": False, "error": "Token has expired"}

    except jwt.InvalidTokenError:
        # token invalid
        return {"valid": False, "error": "Invalid token"}

    except Exception as e:
        return {"valid": False, "error": str(e)}
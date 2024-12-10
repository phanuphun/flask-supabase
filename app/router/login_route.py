import pprint
from flask import Blueprint, jsonify , request
from app.config.supabase_client import supabase
import bcrypt

login_route = Blueprint('login', __name__)

@login_route.route('/register' , methods=['POST'])
def register():
    try:
        body = request.get_json()
        username = body['username']
        password = body['password']
        first_name = body['first_name']
        last_name = body['last_name']
        hash_password = bcrypt.hashpw(password.encode('utf-8'),bcrypt.gensalt(10)).decode('utf-8')

        res = (supabase
            .table('users')
            .insert({
                'username':username,
                'password':hash_password,
                'first_name':first_name,
                'last_name':last_name})
            .execute())
        return jsonify({'msg':'register success','data': res.data}) , 201
        
    except Exception as e : 
        if hasattr(e, 'args') and len(e.args) > 0:
            error_message = e.args[0]
            if 'duplicate key value violates unique constraint' in error_message:
                return jsonify({'msg': 'Username already exists'}), 400
            
        return jsonify({'msg':'error'+str(e)}) , 500

@login_route.route('/login' , methods=['POST'])
def login():
    try:
        body = request.get_json()
        username = body['username']
        password = body['password']
        res_hashed_pass = supabase.table('users').select('password').eq('username',username).execute()
        
        if not res_hashed_pass.data:
            return jsonify({'msg': 'your username or password is incorrect.'}), 401
        
        hashed_pass = res_hashed_pass.data[0]['password']

        if(bcrypt.checkpw(password.encode('utf-8'),hashed_pass.encode('utf-8'))):
            return jsonify({'msg':'login success','token': ''}) , 201
        else:
            return jsonify({'msg':'your username or password is incorrect.'}) , 401
        
    except Exception as e : 
        print(e)
        return jsonify({'msg':'error : '+str(e)}) , 500
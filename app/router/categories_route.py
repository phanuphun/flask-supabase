from flask import Blueprint, jsonify , request
from app.config.supabase_client import supabase

categories_route = Blueprint('categories', __name__)

# get 
@categories_route.route('/categories',methods=['GET'])
def get_categories():
    try:
        res = (supabase
               .table('categories')
               .select('*')
               .execute())
        
        return {'msg':'get data successful!' , 'data':res.data}, 200
    
    except Exception as e:
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
    
# create
@categories_route.route('/categories',methods=['POST'])
def add_category():
    try:
        body = request.get_json()
        name = body['name']
        
        res = (supabase
               .table('categories')
               .insert({'name':name})
               .execute())
        return {'msg':'add new category successful!','data':res.data}, 201
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
    
# update
@categories_route.route('/categories',methods=['PUT'])
def update_category():
    try:
        body = request.get_json()
        id = body['id']
        name = body['name']
        
        res = (supabase
               .table('categories')
               .update({'name':name})
               .eq('id',id)
               .execute())
        return {'msg':'update category successful!','data':res.data}, 201
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
    
# delete
@categories_route.route('/categories',methods=['DELETE'])
def delete_category():
    try:
        body = request.get_json()
        id = body['id']
        
        res = (supabase
               .table('categories')
               .delete()
               .eq('id',id)
               .execute())
        return {'msg':'delete category successful!','data':res.data}, 201
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500

# get books in categories (inner join)
@categories_route.route('/categories/summary', methods=['GET'])
def get_summary():
    try:
        res = (supabase
               .table('categories')
               .select('*,books(*)')
               .execute())
        
        return jsonify({'msg':'get all books in category' , 'data':res.data})
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
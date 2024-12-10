from flask import Blueprint, jsonify , request
from app.config.supabase_client import supabase
import datetime

books_route = Blueprint('books', __name__)

# get
@books_route.route('/books', methods=['GET'])
def get_books():
    try:
        res = (supabase
               .table('books')
               .select('*')
               .execute())
        
        return jsonify({'msg':'get books success!!' , 'data':res.data}) , 200
        
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500

# get book detail
@books_route.route('/books/<string:id>', methods=['GET'])
def get_book_detail(id):
    try:
        res = (supabase
                .table('books')
                .select('*')
                .eq('id',str(id))
                .execute())
        
        return jsonify({'msg':'get books detail success!!' , 'data':res.data}) , 200
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500

# create
@books_route.route('/books',methods=['POST'])
def add_book():
    try:
        body = request.get_json()
        title = body['title']
        price = float(body['price'])
        author = body['author']
        category_id = body['category_id']
        create_date = str(datetime.datetime.now())
        
        res = (supabase
               .table('books')
               .insert({
                   'title':title,
                   'price':price,
                   'author':author,
                   'category_id':category_id,
                   'create_date':create_date
               })
               .execute())

        return jsonify({'msg':'add books success!!' , 'data':res.data}) , 201
        
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
 
# update
@books_route.route('/books',methods=['PUT'])
def update_book():
    try:
        body = request.get_json()
        id = str(body['id'])
        title = body['title']
        price = float(body['price'])
        author = body['author']
        category_id = body['category_id']
        create_date = str(datetime.datetime.now())
        
        res = (supabase
                .table('books')
                .update({
                    'title':title,
                    'price':price,
                    'author':author,
                    'category_id':category_id,
                    'create_date':create_date
                })
                .eq('id',id)
                .execute())
        return jsonify({'msg':'update books success!!' , 'data':res.data}) , 200
    
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
    
# delete
@books_route.route('/books',methods=['DELETE'])
def delete_books():
    try:
        body = request.get_json()
        book_id = body['id'] 
        res = (supabase
               .table('books')
               .delete()
               .eq('id',str(book_id))
               .execute())
        
        return jsonify({'msg':'delete books success!!' , 'data':res.data}) , 200
    except Exception as e :
        print('Error : ',str(e))
        return jsonify('Error : ',str(e)), 500
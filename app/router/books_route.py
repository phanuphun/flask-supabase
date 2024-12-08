from flask import Blueprint, jsonify

books_route = Blueprint('main', __name__)
@books_route.route('/')
def hello_world():
    return '<h1><center>Hello Flask API !!!</center></h1>'

@books_route.route('/books', methods=['GET'])
def get_books():
    return jsonify({"message": "This is the books endpoint."})

# @books_route.route('/books', method=['POST'])
# def method_name():
#     try:
#     except:
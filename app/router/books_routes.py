from flask import Blueprint, jsonify

site_route = Blueprint('main', __name__)
@site_route.route('/')
def hello_world():
    return '<h1><center>Hello Flask API !!!</center></h1>'

@site_route.route('/books', methods=['GET'])
def get_books():
    return jsonify({"message": "This is the books endpoint."})
from flask import Flask , request
app = Flask(__name__)

books = [{'title':'book1','prince':299,'id':1}]

# GET
@app.route('/')
def hello_world():
    q = request.args.get('q')
    print(q)
    return {'msg':'Hello World' , 'params':q} , 200

# POST
@app.route('/book' , methods=['POST','GET','PUT','DELETE'])
def book():
    if request.method == 'POST':
        # body = request.data 
        body = request.get_json()
        books.append(body)
        return {'msg':'add book success','data':books} , 201 
    elif request.method == 'GET':
        return {'data': books}, 200
    elif request.method == 'PUT':
        body = request.get_json()
        print(body)
        for i, book in enumerate(books):
            if book['id'] == body['id']:
                books[i] = body 
        return {'msg':'update success' , 'data' : books} , 200 
    elif request.method == 'DELETE': 
        deleteId = request.args.get('id')
        for i , book in enumerate(books):
            if book['id'] == int(deleteId):
                print('deleted')
                books.pop(i)
        return {'msg':'delete success' , 'data' : books} , 200 
    
    
if __name__ == '__main__' :
    app.run(debug=True)
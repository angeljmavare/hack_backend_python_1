from flask import Flask, jsonify, request
from flask_cors import CORS

users = {'payload':'success'}

app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])  #Hack 1
def users_get():
    if request.method == 'GET':
        return jsonify(users)

@app.route('/user', methods=['POST'])  #Hack 2
def user_post():
    if request.method == 'POST':
        return jsonify(users)
    
@app.route('/user', methods=['DELETE']) #Hack 3
def user_delete():
    if request.method == 'DELETE':
        return jsonify(users)    

@app.route('/user', methods=['PUT'])  #Hack 4
def user_update():
    if request.method == 'PUT':
        global users
        users['error'] = False
        return jsonify(users)

@app.route('/api/v1/users', methods=['GET'])  #Hack 5
def users_v1_get():
    if request.method == 'GET':
        global users
        users['payload']= []
        users.pop('error',None)  #Agregue esta funcion ya que al aplicar el test global me daba error ya que existia el campo 'error' en los siguientes.
        return jsonify(users)
    
@app.route('/api/v1/user', methods=['POST'])  #Hack 6
def user_v1_post():
    if request.method == 'POST':
        email= request.args.get('email')
        name= request.args.get('name')
        global users
        users['payload'] = {'email':email, 'name':name}
        return jsonify(users)
    
@app.route('/api/v1/user/add', methods=['POST'])  #Hack 7
def user_v1_post2():
    if request.method == 'POST':
        email= request.form.get('email')
        name= request.form.get('name')
        id= request.form.get('id')
        global users
        users['payload'] = {'email':email, 'name':name, 'id':id}
        return jsonify(users)
    
@app.route('/api/v1/user/create', methods=['POST'])   #Hack 8
def user_v1_create_post():
    if request.method == 'POST':
        user = request.get_json()
        email = user.get('email')
        name = user.get('name')
        id = user.get('id')
        global users
        users['payload'] = {'email':email, 'name':name, 'id':id}
        return jsonify(users)
    
if __name__ == "__main__":
    app.run(debug=True)
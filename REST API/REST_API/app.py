from flask import Flask,jsonify,request
app = Flask(__name__)


stores = [
    {
    'name': 'D-Mart',
    'items': [
        {'name':'Bags', 'price': 500 },
              { 'name' : 'perfume' , 'price' : 100} ,
              { 'name ': 'Shirts' , 'price' : 600}
    ]
},

{
    'name': 'K-Mart',
    'items': [
              {'name':'Jeans', 'price': 500 },
              { 'name' : 'Jwellery' , 'price' : 100} ,
              { 'name ': 'Jurkins' , 'price' : 600}
    ]
}

]


@app.route('/')
def main():
    return 'Welcome to REST APIs with Python'



# To display all the Stores
@app.route('/stores')
def get_stores():
    return  jsonify({'stores' : stores})



#To check wheter Store is present or not
@app.route('/store/<string:name>')
def check_stores(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'Alert' : 'Sorry,Store not found'})





@app.route('/store', methods=['POST'])
def create_store():
    data = request.get_json()
    new_store = {
        'name': data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify({'Messgae' : 'New Store Successfully Added..!!'})


app.run(port=5060)
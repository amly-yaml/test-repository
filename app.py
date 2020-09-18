from flask import Flask, jsonify, request

stores = [
    {
        'name': 'My Wonderful Store',
        'item': [
            {
                'name': 'Berry',
                'price': '21.22'
            }
        ]
    }
]

app = Flask(__name__)

@app.route('/')
def home():
    return "This is my RestAPI with Flask and Python!"

# GET /stores
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_Store(name):
    # iterate over stores
    for store in stores:
        # if there is store name, return the store name all
        if store['name'] == name:
            return jsonify(store)
    # if none, return error
    return jsonify({'message': 'Store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    # iterate over stores
    for store in stores:
        # if the name match, return the store of item
        if store['name'] == name:
            return jsonify({'item':store['item']})  # 'item' distionary can put or not depend on you want
        # if none, return error message
        return jsonify({'message': 'Item not found in any Store'})
    pass

# Post /store data: {name:}
# just create the new store name
@app.route('/store', methods=['POST'])
def post_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def post_item_to_Store(name):
    # request the data first
    request_data = request.get_json()
    # iterate over stores to get item
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['item'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Item is existed'})


if __name__ == '__main__':
    app.run(port=5000)

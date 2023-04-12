from flask import Flask, jsonify
import pymongo
from pymongo import MongoClient

app = Flask(__name__)

def get_db():
    client = MongoClient(host='mongodb_oep',
                         port=27017, 
                         username='root', 
                         password='pass',
                         authSource="admin")
    db = client["oep_db"]
    return db

# DB
db = get_db()
# Collection : products
products_collection = db.products_tb

@app.route('/')
def ping_server():
    return "Welcome to the world of Old El Passo !"

# Get all products
@app.route('/oep/products')
def get_products():
    products_all = products_collection.find()
    products_dict = [{"name": product["name"]} for product in products_all]
    return jsonify({"products": products_dict})

# Get product
# @app.route('/oep/product/<int:product_id>')
# def get_product(product_id):
#     product = products_collection.find_one({"id": product_id})
#     product_dict = {"name": product["name"]}
#     return jsonify({"product": product_dict})

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)
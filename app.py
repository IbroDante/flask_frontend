from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

API_URL_ITEMS = "http://127.0.0.1:8000/api/items/"
API_URL_SUPPLIERS = "http://127.0.0.1:8000/api/suppliers/"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/items')
def get_items():
    response = requests.get(API_URL_ITEMS)
    items = response.json()
    return jsonify(items)

@app.route('/suppliers')
def get_suppliers():
    response = requests.get(API_URL_SUPPLIERS)
    suppliers = response.json()
    return jsonify(suppliers)

if __name__ == '__main__':
    app.run(debug=True)

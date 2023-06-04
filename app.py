from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)  

receipts = [
    {'id': 1, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/1.jpg', 'store': 'Target', 'total': '0.41', 'status': 'ready'},
    {'id': 2, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/2.jpg', 'store': 'Walmart', 'total': '20.67', 'status': 'ready'},
    {'id': 3, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/3.jpg', 'store': 'Safeway', 'total': '28.52', 'status': 'ready'},
    {'id': 4, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/4.jpg', 'store': 'Walmart', 'total': '54.63', 'status': 'pending'},
    {'id': 5, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/5.jpg', 'store': 'Walmart', 'total': '74.05', 'status': 'pending'},
    {'id': 6, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/6.jpg', 'store': 'Walmart', 'total': '21.08', 'status': 'pending'},
    {'id': 7, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/7.jpg', 'store': 'Target', 'total': '69.69', 'status': 'pending'}
]

# Route to get all receipts
@app.route('/', methods=['GET'])
def landing_page():
    return "Welcome to the Scanner Pro Plus app."

@app.route('/receipts', methods=['GET'])
def get_receipts():
    return jsonify(receipts)

# Route to get a specific receipt by ID
@app.route('/receipts/<int:rec_id>', methods=['GET'])
def get_receipt(rec_id):
    receipt = next((rec for rec in receipts if rec['id'] == rec_id), None)
    if receipt:
        return jsonify(receipt)
    else:
        return jsonify({"message": "Receipt not found"}), 404

if __name__ == '__main__':
    app.run(debug=False)
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)  

receipts = [
    {'id': 1, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/1.jpg', 'store': 'Walmart', 'total': '42.91'},
    {'id': 2, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/2.jpg', 'store': 'Walmart', 'total': '20.67'},
    {'id': 3, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/3.jpg', 'store': 'Walmart', 'total': '222.35'},
    {'id': 4, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/4.jpg', 'store': 'Walmart', 'total': '54.63'},
    {'id': 5, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/5.jpg', 'store': 'Walmart', 'total': '74.05'},
    {'id': 6, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/6.jpg', 'store': 'Walmart', 'total': '21.08'},
    {'id': 7, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/7.jpg', 'store': 'Walmart', 'total': '13.65'}
]

# Route to get all receipts
@app.route('/', methods=['GET'])
def landing_page():
    return "Yooo"

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
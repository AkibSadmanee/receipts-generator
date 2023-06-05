from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)  

receipts = [
    {'id': 1, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/1.jpg', 'store': 'Target', 'total': '0.41', 'status': False, 'date': '05/12/2018', 'logo': f'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/logo/target.png'},
    {'id': 2, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/2.jpg', 'store': 'Walmart', 'total': '20.67', 'status': False, 'date': '--/--/----', 'logo': f'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/logo/walmart.png'},
    {'id': 3, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/3.jpg', 'store': 'Safeway', 'total': '28.52', 'status': False, 'date': '08/04/2022', 'logo': f'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/logo/safeway.png'},
    {'id': 4, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/4.jpg', 'store': '------', 'total': '-.--', 'status': True, 'date': '--/--/----', 'logo': 'https://s3.amazonaws.com/appgyver.assets/composer3/images/image_placeholder.png'},
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
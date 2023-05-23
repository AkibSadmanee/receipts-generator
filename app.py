from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)  

receipts = [
    {'id': 1, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/1.jpg', 'title': 'Image 1', 'label': '10/25/21', 'content': 'Walmart'},
    {'id': 2, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/2.jpg', 'title': 'Image 2', 'label': '10/26/21', 'content': 'Walmart'},
    {'id': 3, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/3.jpg', 'title': 'Image 3', 'label': '10/27/21', 'content': 'Walmart'},
    {'id': 4, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/4.jpg', 'title': 'Image 4', 'label': '10/28/21', 'content': 'Walmart'},
    {'id': 5, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/5.jpg', 'title': 'Image 5', 'label': '10/29/21', 'content': 'Walmart'},
    {'id': 6, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/6.jpg', 'title': 'Image 6', 'label': '10/30/21', 'content': 'Walmart'},
    {'id': 7, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/7.jpg', 'title': 'Image 7', 'label': '10/31/21', 'content': 'Walmart'}
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
from flask import Flask, jsonify, request

app = Flask(__name__)

receipts = [
    {'id': 1, 'url': './images/1.jpg'},
    {'id': 2, 'url': './images/2.jpg'},
    {'id': 3, 'url': './images/3.jpg'},
    {'id': 4, 'url': './images/4.jpg'},
    {'id': 5, 'url': './images/5.jpg'},
    {'id': 6, 'url': './images/6.jpg'},
    {'id': 7, 'url': './images/7.jpg'}
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
    app.run(debug=True)
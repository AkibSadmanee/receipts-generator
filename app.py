# from flask import Flask, jsonify, request

# app = Flask(__name__)

# receipts = [
#     {'id': 1, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/1.jpg'},
#     {'id': 2, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/2.jpg'},
#     {'id': 3, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/3.jpg'},
#     {'id': 4, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/4.jpg'},
#     {'id': 5, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/5.jpg'},
#     {'id': 6, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/6.jpg'},
#     {'id': 7, 'url': 'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/7.jpg'}
# ]

# # Route to get all receipts
# @app.route('/', methods=['GET'])
# def landing_page():
#     return "Yooo"

# @app.route('/receipts', methods=['GET'])
# def get_receipts():
#     return jsonify(receipts[0])

# # Route to get a specific receipt by ID
# @app.route('/receipts/<int:rec_id>', methods=['GET'])
# def get_receipt(rec_id):
#     receipt = next((rec for rec in receipts if rec['id'] == rec_id), None)
#     if receipt:
#         return jsonify(receipt)
#     else:
#         return jsonify({"message": "Receipt not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True, ssl_context='adhoc')



# Importing Flask dependencies
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)  # Defining the application
cors = CORS(app)  # Enabling CORS for Composer compatibility


@app.route('/', methods=['GET'])
def home():
    if(request.method == 'GET'):
        return jsonify({
            "data": "hello world"
        })


# Launching function
if __name__ == '__main__':
    app.run(debug=True)  # Use True for development purposes

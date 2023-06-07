from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)  


receipts = [
    {"store_name": "Evergreen Groceries", "store_address": "4312 Birchwood Lane, Springfield, IL 62704", "store_phone": "(217) 555-4321", "cashier": "Lisa", "date": "06/05/2023", "receipt_number": "827493", "items": [ { "name": "Organic Avocados", "quantity": "4 count", "price": "$6.99" }, { "name": "Grass-fed Ground Beef", "quantity": "1 lb", "price": "$5.99" }, { "name": "Whole Grain Bread", "quantity": "1", "price": "$3.99" }, { "name": "Cage-Free Eggs", "quantity": "1 dozen", "price": "$4.99" }, { "name": "Fuji Apples", "quantity": "2 lbs", "price": "$3.00" }, { "name": "Almond Milk", "quantity": "64 oz", "price": "$2.79" } ], "subtotal": "$27.75", "sales_tax": "$2.29", "total": "$30.04", "payment_method": "Credit Card", "thank_you_message": "Thank you for storeping with us!", "store_tagline": "Evergreen Groceries - Fresh & Local",  "url":  "https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/1.png ",  "id": 1,  "status": False},
    {"store_name": "Page Turner Bookstore", "store_address": "88 Cobblestone Rd, Austin, TX 78745", "store_phone": "(512) 555-7890", "cashier": "Emily", "date": "06/05/2023", "receipt_number": "758925", "items": [ { "name": "'A Promised Land' - Barack Obama", "price": "$24.99" }, { "name": "'Becoming' - Michelle Obama", "price": "$19.99" }, { "name": "'The Code Breaker' - Walter Isaacson", "price": "$21.99" }, { "name": "Moleskine Classic Notebook", "price": "$13.99" } ], "sales_tax": "$9.57", "total": "$125.52", "payment_method": "Cash", "thank_you_message": "Thanks for supporting local bookstores! Happy reading!",  "url":  "https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/2.png ",  "id": 2,  "status": False},
    {"store_name": "The Garden Bistro", "store_address": "4510 Rosewood Drive, Portland, OR 97205", "store_phone": "(503) 555-1234", "server": "Jackson", "date_time": "06/05/2023, 7:35 PM", "receipt_number": "006291", "items": [ { "name": "Grilled Salmon with Lemon Butter", "price": "$21.50", "notes": "Substitute rice for salad" }, { "name": "Rosemary Garlic Roasted Potatoes", "price": "$6.00" }, { "name": "Spinach and Feta Salad", "price": "$12.00" }, { "name": "Chocolate Lava Cake", "price": "$8.50" }, { "name": "Cabernet Sauvignon (Glass)", "price": "$10.00" } ], "tip": "20.00%", "total_before_tax": "$58.00", "tax": "$5.74", "total": "$69.54", "payment_method": "VISA",  "url":  "https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/images/3.png ",  "id": 3,  "status": False}
]
# Route to get all receipts
@app.route('/', methods=['GET'])
def get_receipts():
    return jsonify(receipts)

#curl -X POST -H 'Content-Type: application/json' -d '{"key": "value"}' http://127.0.0.1:5000/test
@app.route('/test', methods=['POST'])
def get_abcd():
    print(request.get_json())
    return 'success!!'


if __name__ == '__main__':
    app.run(debug=False)



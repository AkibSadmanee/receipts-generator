from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import re


app = Flask(__name__)
cors = CORS(app)  
def intersection(companyName_1, companyName_2):
    return companyName_1.intersection(companyName_2)

def union(companyName_1, companyName_2):
    return companyName_1.union(companyName_2)

def jaccard_similarity(companyName_1, companyName_2): 
    words_companyName_1_set = set(companyName_1)
    words_companyName_2_set = set(companyName_2)
    intersection_companyNames = intersection(words_companyName_1_set, words_companyName_2_set)
    union_companyNames = union(words_companyName_1_set, words_companyName_2_set)
    return len(intersection_companyNames) / len(union_companyNames)

stores = ["samsclub","7eleven","islandvintage","ross","abc","jackinthebox","safeway","apple","kfc","starbucks","bestbuy","subway","burgerking","lnlhawaiianbarbecue","tacobell","costcowholesale","longsdrugs","target","dominos","macys","times","donquijote","mcdonalds","walmart","downtoearth","mcdonalds","wendys","foodlandfarms","pandaexpress","wholefoods","hmart","papajohns","zippys","homedepot","pizzahut"] 

receipts = [
    { "ReceiptInfo": { "merchant": "COSTCO WHOLESALE", "address": "525 Alakawa St, Honolulu, HI 96817", "date": "04/15/2023", "city": "Honolulu", "state": "HI", "phoneNumber": None, "tax": 6.19, "total": 137.66, "ITEMS": [ { "description": "ORG RICED", "quantity": 1, "unitPrice": 8.69, "totalPrice": 8.69 }, { "description": "BANANAS", "quantity": 1, "unitPrice": 2.39, "totalPrice": 2.39 }, { "description": "DUBLINER CHS", "quantity": 1, "unitPrice": 13.07, "totalPrice": 13.07 }, { "description": "KS BLUEBERRY", "quantity": 1, "unitPrice": 8.99, "totalPrice": 8.99 }, { "description": "QUESO CRUNCH", "quantity": 1, "unitPrice": 3.00, "totalPrice": 3.00 }, { "description": "PANKO SHRIMP", "quantity": 1, "unitPrice": 20.49, "totalPrice": 20.49 }, { "description": "CHICKEN BAKE", "quantity": 1, "unitPrice": 12.79, "totalPrice": 12.79 }, { "description": "QUESO CRUNCH", "quantity": 1, "unitPrice": 3.00, "totalPrice": 3.00 }, { "description": "KS PISTACHIO", "quantity": 1, "unitPrice": 14.99, "totalPrice": 14.99 }, { "description": "KS SUP PIZZA", "quantity": 1, "unitPrice": 11.79, "totalPrice": 11.79 }, { "description": "PARMIGIANO", "quantity": 1, "unitPrice": 13.99, "totalPrice": 13.99 }, { "description": "HEALTHYNOODL", "quantity": 1, "unitPrice": 16.29, "totalPrice": 16.29 }, { "description": "CAGE FREE", "quantity": 1, "unitPrice": 5.99, "totalPrice": 5.99 } ] } },
    { "ReceiptInfo": { "merchant": "MCCULLY BICYCLE & SPORTING", "address": "2124 SOUTH KING ST.", "date": "12/18/2022", "city": "HONOLULU", "state": "HI", "phoneNumber": "955-6329", "tax": 18.96, "total": 436.44, "ITEMS": [ { "description": "22 XTC JR 24 LITE ECLIPSE", "quantity": 1, "unitPrice": 399.98, "totalPrice": 399.98 }, { "description": "BICYCLE LICENSE", "quantity": 1, "unitPrice": 15.00, "totalPrice": 15.00 }, { "description": "STICKY BUMPS SURF WAX", "quantity": 1, "unitPrice": 2.50, "totalPrice": 2.50 } ] } }
]
# Route to get all receipts
@app.route('/', methods=['GET'])
def get_receipts():
    return jsonify(receipts)


@app.route('/<company_name>', methods=['GET'])
def get_logo(company_name):
    processed_company_name = re.sub('[^a-zA-Z0-9]', '', company_name.lower())
    j_sims = [jaccard_similarity(processed_company_name, s) for s in stores]
    search_name = stores[j_sims.index(max(j_sims))]

    url = f'https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/static/logos/{search_name}.jpg'
    # Update an existing user with the provided user ID
    if max(j_sims) > 0.55:
        return jsonify(url)
    return jsonify("https://raw.githubusercontent.com/AkibSadmanee/receipts-generator/main/static/LogoHead.png")

if __name__ == '__main__':
    app.run(debug=False)



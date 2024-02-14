from flask import Flask, request, jsonify

app = Flask(__name__)

def find_unauthorized_sales(product_listings, sales_transactions):    
    # create dictionary mapping product IDs to their authorized seller IDs
    authorized_sellers = {pl['productID']: pl['authorizedSellerID'] for pl in product_listings}

    unauthorized_sales = []
    # iterate through sale transactions
    for transaction in sales_transactions:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']

        # determine if a sale was made by an unauthorized seller by checking if seller ID is same as authorized seller ID for each product ID
        if authorized_sellers[product_id] != seller_id:
            unauthorized_sales.append({"productID": product_id, "unauthorizedSellerID": seller_id})

    return unauthorized_sales


# specifies URL path that route will handle and route will only respond to http POST request
@app.route('/unauthorized_sales', methods=['POST'])
def unauthorized_sales():
    try:
        # make sure that the endpoint process request containing JSON data
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return jsonify({"message": 'Content-Type not supported!'}), 400

        # extracts JSON data from request body and converts it into dictionary
        data = request.get_json()

        product_listings = data['productListings']
        sales_transactions = data['salesTransactions']

        # it exists function will return all unauthorized sales
        unauthorized_sales = find_unauthorized_sales(product_listings, sales_transactions)
        if unauthorized_sales:
            response = {"unauthorizedSales": unauthorized_sales}
            return jsonify(response), 200
        else:
            return jsonify({"message": "No unauthorized sales detected"}), 200

    # handling errors that might appear
    except KeyError as e:
        return jsonify({"message": f"JSON data is missing key: {e}"}), 400
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 400


if __name__ == '__main__':
    # debug=True enables Flask's debug mode for development purposes
    app.run(debug=True)  
    
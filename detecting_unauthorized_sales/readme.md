# Detecting unauthorized sales

This Flask application is designed to detect unauthorized sales transactions by comparing product listings with sales transactions.
It exposes an endpoint `/unauthorized_sales` that accepts JSON data that should contain product listings and sales transactions, analyzes the data, and returns if any unauthorized sales are detected.

## Endpoint
    - URL: /unauthorized_sales
    - Method: POST
    - Content-Type: application/json


## Running the app
Make sure that you have installed Flask. I recommend to create new environment where you will install Flask.
``` python3 -m venv <name_of_virtualenv> ```

Once you have created an envionment activate it and install Flask.
``` pip install Flask ```

Activate the environment:
on Linux: ``` source ./path/to/your/environment/bin/activate ```

Run the app in your terminal:
``` python app.py ```

## Sending POST request to test the app
### using curl
- open a new terminal
- paste: ``` curl -X POST http://127.0.0.1:5000/unauthorized_sales -H 'Content-Type: application/json' -d '{ "productListings": [{"productID": "toy12", "authorizedSellerID": "A1"}, {"productID": "car12", "authorizedSellerID": "Joe"}, {"productID": "brush11", "authorizedSellerID": "Bobby"}],"salesTransactions": [{"productID": "toy12", "sellerID": "A1"}, {"productID": "car12", "sellerID": "Joe"}, {"productID": "brush11", "sellerID": "Bobby"}]}' ```
- change sellerIDs to see different responses


### using Postman:
- download the Postman app
- open the app, click `New`, then `HTTP` Request and choose `POST` on dropdown arrow
- next to POST paste URL ``` http://127.0.0.1:5000/unauthorized_sales ```
- in `Headers` under `Key` write `Content-Type` and under `Value` write `application/json`
- go to `Body` next to `Headers`
- choose `raw` radio button and `JSON` from dropdown arrow
- paste ``` {
  "productListings": [{"productID": "toy12", "authorizedSellerID": "A1"}, {"productID": "car12", "authorizedSellerID": "Joe"}, {"productID": "brush11", "authorizedSellerID": "Bobby"}],
  "salesTransactions": [{"productID": "toy12", "sellerID": "A1"}, {"productID": "car12", "sellerID": "Joe"}, {"productID": "brush11", "sellerID": "Bobby"}]
} ```
- click on `Send` and whatch for messages in the lower section of the app and in terminal where you run app.py
- change sellerIDs to see different responses

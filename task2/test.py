import requests

BASE = "http://127.0.0.1:5000/"

request = { "productListings": [{"productID": "123", "authorizedSellerID": "A1"}],
            "salesTransactions": [{"productID": "123", "sellerID": "B2"}]}

responce = requests.post(BASE + "saledetector", json=request)
print(responce.json())
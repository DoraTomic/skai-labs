from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

root_parser = reqparse.RequestParser()
root_parser.add_argument("productListings", type=dict, required=True)
root_parser.add_argument("salesTransactions", type=dict, required=True)

message_parser1 = reqparse.RequestParser()
message_parser1.add_argument('productID', type=str, location=('productListings',), required=True)
message_parser1.add_argument('authorizedSellerID', type=str, location=('productListings',), required=True)
message_parser2 = reqparse.RequestParser()
message_parser2.add_argument('productID', type=str, location=('salesTransactions',), required=True)
message_parser2.add_argument('sellerID', type=str, location=('salesTransactions',), required=True)


class SaleDetector(Resource):
    def post(self):
        
        root_args = root_parser.parse_args()
        message_args1 = message_parser1.parse_args(req=root_args)
        message_args2 = message_parser2.parse_args(req=root_args)
        
        if(message_args1['productID'] == message_args2['productID']):
            if(message_args1['authorizedSellerID'] != message_args2['sellerID']):
                sale = {"unauthorizedSales": [{"productID": message_args2['productID'], "unauthorizedSellerID": [message_args2['sellerID']]}]}
            else:
                sale = {"unauthorizedSales": "None"}
        else:
            return {"message": "productID must mach!"}, 400
        return sale, 200


api.add_resource(SaleDetector, "/saledetector")

if __name__ == "__main__":
    app.run(debug=True)
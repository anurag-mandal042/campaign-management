from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
from campaigns import campaigns
app = Flask(__name__)
api = Api(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


class Campaign(Resource):
    def get(self):
        return {"status": "Success", "data": campaigns}


api.add_resource(Campaign, "/getCampaignList/")

if __name__ == "__main__":
    app.run()

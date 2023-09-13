from flask_cors import CORS
from flask import Flask , request,jsonify
from pymongo import MongoClient

app=Flask(__name__)
CORS(app)

@app.route('/one', methods=['GET'])
def one():
    values = [
        {'category_name':"Hello, one",'img_url':"111111111111000000022235"}
    ]
    return jsonify(values)

@app.route('/two', methods=['GET'])
def two():
    values = [
        {'category_name':"Hello two, Wallpaper Build try",'img_url':"22222222222222"}
    ]
    return jsonify(values)


if __name__=="__main__":
    app.run(host="0.0.0.0",debug=True)



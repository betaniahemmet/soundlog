from flask import Flask, request, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError
from datetime import datetime
from bson import json_util

app = Flask(__name__)

# Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['amp_data']
collection = db['measurements']

# Create index on the timestamp field
# collection.create_index('timestamp')
# collection.drop()

def parse_json(data):
    '''Turns the data into json format'''
    return json_util.dumps(data)

@app.route('/measurements', methods=['POST'])
def store_measurement():
    '''Recieve data from pico'''
    data = request.get_json()  # Get JSON data from request payload
    pico_id = data.get('pico_id') # Extract the id of the pico
    value = data.get('value')  # Extract the measurement value
    timestamp = data.get('timestamp')  # Extract the timestamp
    
    if not all([pico_id, value, timestamp]):
        return jsonify({'error': 'Invalid request payload'}), 400

    # Store the measurement in MongoDB with the timestamp
    document = {'pico_id': pico_id, 'value': value, 'timestamp': timestamp}
    
    try:
        result = collection.insert_one(document)
        inserted_id = str(result.inserted_id)
        return jsonify({'message': 'Measurement stored successfully', 'inserted_id': inserted_id}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/measurements', methods=['GET'])
def get_measurements():
    measurements = [parse_json(i) for i in collection.find()]
    return measurements, 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

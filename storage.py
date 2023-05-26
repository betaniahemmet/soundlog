from pymongo import MongoClient
from config import database
from time import time
from datetime import datetime, timedelta

def store_reading(collection, value, sensor_id):
    """Store a sensor reading in the database"""
    new_reading = {"unix_time": time(), "sensor_id": sensor_id, "recorded_value": value}
    print(collection)
    result = collection.insert_one(new_reading).inserted_id
    print(result)

def find_reading(collection, first_timestamp, second_timestamp):
    """Find readings between two unix time stamps"""
    fetched_data = [
        i for i in collection.find(
            {"unix_time": {"$gte": first_timestamp, "$lt": second_timestamp}}
        )
    ]
    return fetched_data


def get_readings_by_week(collection, year, iso_week):
    """Retrieve readings from the database for a given year and ISO week number"""
    # Get the start and end dates of the ISO week
    start_date = datetime.strptime(f'{year}-W{int(iso_week):02d}-1', '%G-W%V-%u')
    end_date = start_date + timedelta(days=6)
    
    # Convert dates to Unix timestamps
    start_timestamp = start_date.timestamp()
    end_timestamp = end_date.timestamp()
    
    # Query the database for readings within the specified timestamp range
    fetched_data = [
        i for i in collection.find(
            {"unix_time": {"$gte": start_timestamp, "$lt": end_timestamp}}
        )
    ]
    
    return fetched_data


def main():

    """Connect to database"""
    with MongoClient(host="localhost", port=27017) as client:
        db = client.amp_data # The name of the database is amp_data
        readings = db.readings # The name of the collection is readings
        # store_reading(readings, i, 1252)
        '''
        docs = find_reading(readings, 1685093032.3821669, 1685093033.0)
        print(docs)
 
        docs = find_reading(readings, 99999999999, 0)
        print(docs)

        docs = [i for i in readings.find()]
        print(docs)
        '''
        week_readings = get_readings_by_week(readings, 2023, 21)
        print(week_readings)

if __name__ == "__main__":
    main()

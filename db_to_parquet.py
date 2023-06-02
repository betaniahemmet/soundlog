from pymongo import MongoClient
import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd
from bson import json_util


# Configure MongoDB connection
client = MongoClient('mongodb://localhost:27017')
db = client['amp_data']
collection = db['measurements']


def parse_json(data):
    return json_util.dumps(data)

def main():

    #data = [parse_json(i) for i in collection.find()]
    #print(data)
    df = pd.DataFrame(list(collection.find({})))
    df = df.astype({"_id": str})
    #print(df)
    table = pa.Table.from_pandas(df)
    print(table)
    #pq.write_table(table, 'amplitude.parquet')


    print("The data was successfully stored in 'amplitude.parquet'")


if __name__ == '__main__':
    main()

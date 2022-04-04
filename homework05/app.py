from flask import Flask, request, jsonify
import json
import logging
import redis

app = Flask(__name__)
meteorite_data = {}


@app.route('/data',methods=['POST'])
def read_data():
    """
    This function reads the meteorite landings data and then lets the user know that the file has been read in.
    """

    global meteorite_data

    rd = redis.Redis(host='172.17.0.8', port=6379)
    
    logging.info("Reading data from file.")
    
    with open('ML_Data_Sample.json' , 'r') as f:
        meteorite_data = json.load(f)
   
    return f'Data has been read from file\n'

@app.route('/data', methods=['GET'])
def all_names():
    """
    This function iterates through a list of meteorite landings within the file that was read in.
    
    Returns:
        A list of names
    """
    rd = redis.Redis(host='172.17.0.8', port=6379)
   
    logging.info("connecting to route for names")
   
    data = []

    for row in meteorite_data['meteorite_landings']:
        data.append(row)

   # BONUS PART 

   # data = []

   # start = request.args.get('start', 0)

   # try:

   #     start = int(start)
   # 
   # except ValueError:
   #     return f'invalid start value, must be an integer.\n'
   
   # while start <= len(meteorite_data['meteorite_landings']) + 10000:
   #     pos = start-10001
   #     data.append(meteorite_data['meteorite_landings'][pos])
   #     start += 1;

    
    return jsonify(data)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0') 



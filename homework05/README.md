# REDIS METEORITE DATA
## How to Start a Redis Database
run the following command within your terminal:

    docker run -d -p PORT_NUMBER:6379 -v $(pwd)/data:/data:rw --name=YOUR_USER_NAME-redis redis:6 --save 1 1

## How to pull/build/launch the Flask app
After downloading my repository execute the following three commands within your terminal:

    export FLASK_APP=app.py
    export FLASK_ENV=development
    flask run -p YOUR_PORT_NUMBER

## How to perform post and get requests
Once you have your flask server up and running you will need to open up a new terminal.
There are two options for commands, one is the get method and the other uses a post method. The post method reads data into the server for the get method to use. The data I used can be found [here.](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json)
To output the data, use the get method. Examples of the two commands are as follows:

    curl localhost:YOUR_PORT_NUMBER/data -X POST
    curl localhost:YOUR_PORT_NUMBER/data
## What does the data mean?
The data output will look something like this:

     {
    "GeoLocation": "(-60.7340, 54.3187)",
    "id": "10297",
    "mass (g)": "8670",
    "name": "Thomas",
    "recclass": "H6",
    "reclat": "-60.7340",
    "reclong": "54.3187"
  

    },
    {
      "GeoLocation": "(-61.5820, -10.3998)",
      "id": "10298",
      "mass (g)": "801",
      "name": "Agnes",
      "recclass": "H6",
      "reclat": "-61.5820",
      "reclong": "-10.3998"
    },
Each of the data points contains:
1. The name of the meteor
2. The id of the meteor
3. The mass of the meteor in grams
4. The class of the meteor (ie: what material the meteor was composed of)
5. The latitude of the meteor "reclat"
6. The longitude of the meteor "reclong"
7. The combined coordinates of the meteor "GeoLocation"

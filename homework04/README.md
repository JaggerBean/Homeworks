# Analizing meteorite landing data

## :grey_question: What is this repo

This repo contains a python script that takes a dictionary of data points on meteorite landings and calculates the average mass of them, where they landed, and how many of each type of meteor there was.\
The test script is used to test the 'ml_data_analysis.py' script.

## :open_file_folder:How to get test data

To get some test data for the script, run this on your terminal in the desired directory.

```
   wget https://raw.githubusercontent.com/tacc/coe-332-sp22/main/docs/unit04/scripts/Meteorite_Landings.json
```

## :page_facing_up:Script Explanation

### ml_data_analysis.py

This script reads over a `.json` dictionary that contains meteorite data.\
It then calculates the average mass of all of the meteorites.\
Next it finds the hemispheres of each of the meteorites and calculates how many meteorites were in each hemisphere.\
Lastly it reads what kind of meteor class each meteor belongs to and counts how many meteors were found in each of those classes.\

### test_ml_data_analysis.py

This script tests `ml_data_analysis.py`

## :runner:Running the Program

### If you would like to use my docker image from docker hub, follow these steps in order on your terminal

```
   docker pull jaggerbean/ml_data_analysis:hw04
```
### If you would like to build your own docker image, follow these steps in order on your terminal

```
   docker build -t username/ml_data_analysis:1.0 .
```
Under `username` you can put your own docker hub id.\
You may replace `ml_data_analysis` with whatever name for the image you would like.\
The part after the `:` is the version number. You can make that anything you want.

Make sure not to forget the `.` at the end! This is necessary to give the image a path.

### How to run the script

Follow the following steps on your terminal:

```
   docker run --rm -v $PWD:/data jaggerbean/ml_data_analysis:hw04 ml_data_analysis.py /data/Meteorite_Landings.json
```
Remember, if you changed any of the names for the docker image previously when making your own docker image, change them accordingly within the command!

The output should look like:
```
Summary data following meteorite analysis:

Average mass of meteors:
83857.3 grams

Hemisphere summary data:
there were 21 meteors found in the Northern & Eastern quadrant
there were 6 meteors found in the Northern & Western quadrant
there were 0 meteors found in the Southern & Eastern quadrant
there were 3 meteors found in the Southern & Western quadrant

Class summary data:
The L5 Class was found 1 time(s)
The H6 Class was found 1 time(s)
The EH4 Class was found 2 time(s)
The Acapulcoite Class was found 1 time(s)
The L6 Class was found 6 time(s)
The LL3-6 Class was found 1 time(s)
The H5 Class was found 3 time(s)
The L Class was found 2 time(s)
The Diogenite-pm Class was found 1 time(s)
The Stone-uncl Class was found 1 time(s)
The H4 Class was found 2 time(s)
The H Class was found 1 time(s)
The Iron-IVA Class was found 1 time(s)
The CR2-an Class was found 1 time(s)
The LL5 Class was found 2 time(s)
The CI1 Class was found 1 time(s)
The L/LL4 Class was found 1 time(s)
The Eucrite-mmict Class was found 1 time(s)
The CV3 Class was found 1 time(s)
```
#### If you want to use your own data

Simply change the `/data/Meteorite_landings.json` path to `/data/<yourfilename>.json`.

### How to run `test_ml_data_analysis.py`

Follow these steps in your terminal.
``
   docker run --rm -v $PWD:/data jaggerbean/ml_data_analysis:hw04 pytest /code
``
Once again change any naming discrepancies you may have with your docker image.

The output should look like:
```
============================= test session starts ==============================
platform linux -- Python 3.6.8, pytest-7.0.0, pluggy-1.0.0
rootdir: /code
collected 6 items

code/test_ml_data_analysis.py ......                                     [100%]

============================== 6 passed in 0.05s ===============================
```

## How to format your own `.json` library

The .json library used looks like:
```
{
    "meteorite_landings": [
      {
        "name": "Ruiz",
        "id": "10001",
        "recclass": "L5",
        "mass (g)": "21",
        "reclat": "50.775",
        "reclong": "6.08333",
        "GeoLocation": "(50.775, 6.08333)"
      },
      {
        "name": "Beeler",
        "id": "10002",
        "recclass": "H6",
        "mass (g)": "720",
        "reclat": "56.18333",
        "reclong": "10.23333",
        "GeoLocation": "(56.18333, 10.23333)"
      }
    ]
}
```
You can also see a full example file [Here](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json)

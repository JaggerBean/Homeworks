# Hello, <img src="https://raw.githubusercontent.com/MartinHeinz/MartinHeinz/master/wave.gif" width="30px"> This repo contains Jagger Bean's homework03 submission for COE332


# What is the purpose?
This repo contains 2 python files. These files calculate the turbidity of water and the time until is safe to drink given json data of the water.

to download the json data set that was used in these files visit https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json

read_turbidity.py reads the turbidity data from the json file. It then calculates the average turbidity from the last 5 data sets. Then it uses this average turbidity to calculate the time remaining until the water is safe to drink. 
test_turbidity.py tests the functions within read_turbidity.py to make sure that they are working as intended.

to run this code make sure that your json file is named turbidity_data.json. Then simply run the read_turbidity.py script. To test the functions just run a pytest command.


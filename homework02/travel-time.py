import json
import math


robot_location_lat = 16.0
robot_location_lon = 82.0



mars_radius = 3389.5    # km

def calc_gcd(latitude_1: float, longitude_1: float, latitude_2: float, longitude_2: float) -> float:

	lat1, lon1, lat2, lon2 = map( math.radians, [latitude_1, longitude_1, latitude_2, longitude_2] )
    
	d_sigma = math.acos( math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(abs(lon1-lon2)))

	return ( mars_radius * d_sigma )



def check_comp(dict_list, composition):

	total_time = 0.


	if (dict_list[a][composition] == "stony"):
		
		total_time = total_time + 1
		sample_time = 1.
					
	if(dict_list[a][composition] == "iron"):
		total_time = total_time + 2
		sample_time = 2.

	if(dict_list[a][composition] == "stony-iron"):
		total_time = total_time + 3
		sample_time = 3.		

	return(sample_time)




with open('sites.json', 'r') as f:
	ml_data = json.load(f)

i = 1
a = 0

distance = 0.

time = 0.

travel_time = 0.

site_time = 0.

total_site_time = 0.

total_distance = 0.


for row in ml_data['sites']:
	
	total_site_time = total_site_time + check_comp(ml_data['sites'], 'composition')	
	site_time = check_comp(ml_data['sites'], 'composition') 


	if(ml_data['sites'][0] == row):
	
		total_distance = total_distance + (calc_gcd(robot_location_lat, robot_location_lon, float(row['latitude']), float(row['longitude'])))
		distance = (calc_gcd(robot_location_lat, robot_location_lon, float(row['latitude']), float(row['longitude'])))		


		print("leg = 1 , Time to travel = ", distance/10., " hr, Time spent on sample = ", site_time, " hr")
	else:
			
		row2 = ml_data['sites'][i-2]
		row3 = ml_data['sites'][i-1]


		total_distance = total_distance + calc_gcd(float(row2['latitude']), float(row2['longitude']), float(row3['latitude']), float(row3['longitude']))	
		distance = (calc_gcd(robot_location_lat, robot_location_lon, float(row['latitude']), float(row['longitude'])))		

		print("leg =", i, ", Time to travel = ", distance/10., " hr, Time spent on sample = ", site_time, " hr")


	if(i<5):
		i = i+1
		a = a+1		

travel_time = total_distance/10

time = travel_time + total_site_time


print("total time elapsed = ", time)

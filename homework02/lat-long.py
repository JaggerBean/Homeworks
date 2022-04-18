import random
import json

lat1 = random.uniform(16.0, 18.0)
lon1 = random.uniform(82.0, 84.0)

lat2 = random.uniform(16.0, 18.0)
lon2 = random.uniform(82.0, 84.0)

lat3 = random.uniform(16.0, 18.0)
lon3 = random.uniform(82.0, 84.0)

lat4 = random.uniform(16.0, 18.0)
lon4 = random.uniform(82.0, 84.0)

lat5 = random.uniform(16.0, 18.0)
lon5 = random.uniform(82.0, 84.0)



composition1 = random.choice(["stony", "iron", "stony-iron"])

composition2 = random.choice(["stony", "iron", "stony-iron"])

composition3 = random.choice(["stony", "iron", "stony-iron"])

composition4 = random.choice(["stony", "iron", "stony-iron"])

composition5 = random.choice(["stony", "iron", "stony-iron"])





data = {}
data['sites'] = []
data['sites'].append( {'site_id': 1, 'latitude': lat1, 'longitude': lon1, 'composition': composition1 } )

data['sites'].append( {'site_id': 2, 'latitude': lat2, 'longitude': lon2, 'composition': composition2 } )

data['sites'].append( {'site_id': 3, 'latitude': lat3, 'longitude': lon3, 'composition': composition3 } )

data['sites'].append( {'site_id': 4, 'latitude': lat4, 'longitude': lon4, 'composition': composition4 } )

data['sites'].append( {'site_id': 5, 'latitude': lat5, 'longitude': lon5, 'composition': composition5 } )









with open('sites.json', 'w') as out:
    json.dump(data, out, indent=2)

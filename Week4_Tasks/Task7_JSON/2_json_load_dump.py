
import json

# load method -> load a JSON file into python object
with open('KF_training/Week4_Tasks/Task7_JSON/states.json') as f:
    data = json.load(f)

for state in data['states']:
    print(state['name'],state['abbreviation'])
    del[state['area_codes']]


# dump method -> dump the data into JSON file without abbrevation

with open('KF_training/Week4_Tasks/Task7_JSON/new_states.json','w') as f:
    json.dump(data,f,indent=2)

    




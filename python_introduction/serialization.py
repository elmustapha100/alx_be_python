#Serialization in python means the process of converting a python objects into an easily transmitted or storage system
#like a storage byte stream e.g packaging your items in a box for relocating 
# Create a Python function called process_json(data: dict, filename: str) -> dict that does the following:

# Takes a dictionary (data) and a filename (filename) as input.
# Serializes the dictionary to a JSON file with the given filename.
# Deserializes the JSON file back into a dictionary.
# Returns the deserialized dictionary.


import json

#A dictionary python object 
data = {'name': 'Alice', 'age': 30, 'city': 'Kampala'}
#Serializing into a JSON string 
json_string = json.dumps(data)

with open('data.json','a') as file : 
    json.dump(data,file)
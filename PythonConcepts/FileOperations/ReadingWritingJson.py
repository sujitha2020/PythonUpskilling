import json
 
# Data to be written
dictionary = {
    "name": "abc",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "1234567891"
}
 
with open("sample.json", "w") as outfile:
    json.dump(dictionary, outfile)
    
# Opening JSON file
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json_object)
print(type(json_object))

#json.load() takes a file object and returns the json object. It is used to read JSON encoded data from a file and convert it into a Python dictionary

# json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary. It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.

# JSON string: 
# Multi-line string 
data = """{ 
    "Name": "Jennifer Smith", 
    "Contact Number": 7867567898, 
    "Email": "jen123@gmail.com", 
    "Hobbies":["Reading", "Sketching", "Horse Riding"] 
    }"""
    
# parse data: 
res = json.loads( data ) 
    
# the result is a Python dictionary: 
print( res )
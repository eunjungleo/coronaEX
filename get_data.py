import json
import xmltodict
 
with open("raw_data.xml",'r') as f:
    xmlString = f.read()
 
print("xml input (raw_data.xml):")
print(xmlString)
 
jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)
 
print("\nJSON output(output.json):")
print(jsonString)
 
with open("data.json", 'w') as f:
    f.write(jsonString)
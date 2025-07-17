import yaml
import json
from json2xml import json2xml
import xmlschema

with open('../base.json', 'r') as file:
    json_data = json.load(file)

# 1. json to yaml
with open('./base.yaml', 'w') as yaml_file:
    yaml.dump(json_data, yaml_file)

# 2. json to xml
xml_str = json2xml.Json2xml(json_data, attr_type=False).to_xml()
with open('./base.xml', 'w') as xml_file:
    xml_file.write(xml_str)

# 3. validate xml with xsd
schema = xmlschema.XMLSchema('./base.xsd') 
is_xml_valid = schema.is_valid('./base.xml')

print(f"Is the XML Valid?: {is_xml_valid}")
import xml.etree.ElementTree as ET

# Read from the XML file ..
xmlDocument = ET.parse('Week3_4_data.xml')
actions = xmlDocument.getroot()

for action in actions:

    numberOfSides = action.get('numberOfSides')
    length = action.get('length')

    print("numberOfSides = {}, length = {}".format(numberOfSides, length))


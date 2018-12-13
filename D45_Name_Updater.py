import xml.etree.ElementTree as ET

tree = ET.parse('BlockF.EPConfig')
root = tree.getroot()

for child in root:
	if (child.tag=="EPuserList" or child.tag=="EPuserListCode"):
		surname = child.find('Surname')
		name = child.find('Name')
		callcode = child.find('Apartaddress')
		if surname.text == "Unit":
			print("Node already modified")
			continue
		else:
			newsurname = "Unit"
			newname = callcode.text.lstrip('0')
			print("Modifying Node. Old name was "+surname.text+" "+name.text+". New name is "+newsurname+" "+newname)
			surname.text = newsurname
			name.text = newname
tree.write('outputF.EPConfig')
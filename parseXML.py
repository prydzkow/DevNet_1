import xml.etree.ElementTree as ET #call it ET

tree = ET.parse('sampleFile.xml')

#get the root element of the file and store it in 'root'
root = tree.getroot()

#print(root.tag)
#print(root.attrib)
#print(root[0].text)
#print(root[1][0].text)
for child in root:
    print(child.tag, child.attrib)
    for element in child:
        print(element.tag, element.attrib, element.text)
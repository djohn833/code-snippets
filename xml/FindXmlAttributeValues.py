import sys
import xml.etree.ElementTree as ET


elemName = sys.argv[1]  # e.g., {http://schemas.telerik.com/2008/xaml/presentation}RadDatePicker
attrName = sys.argv[2]  # e.g., Width
filename = sys.argv[3]


doc = ET.parse(filename)
for node in doc.getroot().iter(elemName):
    if attrName in node.attrib:
        print('{0}: {1}'.format(sys.argv[1], node.attrib[attrName]))

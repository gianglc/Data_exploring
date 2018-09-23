from xml.dom import minidom

xmldoc = minidom.parse("biking3-15-2012.tcx.xml")

biking_data = xmldoc.getElementsbyTagName("Trackpoint")[0]

# Time info
time = biking_data.getElementsbyTagName("Time")[0]
time_dat = time.firstChild.data

# Lat Long Info 
pos = biking_data.getElementsbyTagName("Pos")[0]
lat = biking_data.getElementsbyTagName("LatitudeDegrees")[0]
lon = biking_data.getElementsbyTagName("LongitudeDegrees")[0]

lat_dat = lat.firstChild.data
lon_dat = lon.firstChild.data






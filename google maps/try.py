import requests
import xml.etree.ElementTree as ET


def get_data():

    data = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    root = ET.fromstring(data.content)    

    latlon = []
    count = 0
    j = 0
    for i in root:
        st_name = root[j][0].text
        st_lat = root[j][2].text
        st_lon = root[j][3].text

        if st_lat != "0" and st_lon != "0":
            latlon.append([st_name, float(st_lat), float(st_lon)])
        j += 1

    print(latlon)

get_data()

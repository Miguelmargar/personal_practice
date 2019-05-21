import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template





app = Flask(__name__)

@app.route('/')
def main():
    return render_template("googleMaps.html")




def get_data():

    data = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    root = ET.fromstring(data.content)    
    
    j = 0
    for i in root:
        st_name = root[j][0].text
        st_lat = root[j][2].text
        st_lon = root[j][3].text
        print(st_name + " is at: " + st_lat + ", " + st_lon)
        j += 1  

#get_data()

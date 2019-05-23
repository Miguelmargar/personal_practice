import requests
import xml.etree.ElementTree as ET
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def main():
    latLonStations = get_data()
    return render_template('googleMaps.html', latLonStations=latLonStations)




def get_data():

    data = requests.get("http://api.irishrail.ie/realtime/realtime.asmx/getAllStationsXML")
    root = ET.fromstring(data.content)    

    latLonStations = []
    count = 0
    j = 0
    for i in root:
        st_name = root[j][0].text
        st_lat = root[j][2].text
        st_lon = root[j][3].text

        if st_lat != "0" and st_lon != "0":
            latLonStations.append([st_name, float(st_lat), float(st_lon)])
        j += 1

    return latLonStations 


if __name__ == '__main__':
    app.run(debug=True)

#set FLASK_APP=api.py
#export FLASK_ENV=development
import folium
import pandas as pd
map = folium.Map([26,80], zoom_start=6) 
#Defining a FeatureGroup
fg = folium.FeatureGroup(name='My Map')
data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+'m', radius=10,
        fill_color=get_color(el), color='grey', opacity=0.5))
map.add_child(fg)
map.save('Map1.html')

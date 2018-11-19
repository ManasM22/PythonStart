import folium, pandas as pd
#getting DATA
data = pd.read_csv('Volcanoes.txt')
lat = list(data['LAT'])
lon = list(data['LON'])
elev = list(data['ELEV'])

#Getting color for marker
def get_color(elevation):
    if elevation<1000:
        return 'green'
    if elevation<3000:
        return 'orange'
    return 'red'

#Creating MAP with initial coordinates
map = folium.Map([26,80], zoom_start=8)

#Storing MARKERS in featuregroup
fg = folium.FeatureGroup(name='My Map')
for lt,ln,el in zip(lat,lon,elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln], popup=str(el)+'m', radius=6,
        fill_color=get_color(el), color='grey', opacity=0.7))

#Displayng Polygons over countries
fg2 = folium.FeatureGroup(name='Polygon')
fg2.add_child(folium.GeoJson(data=open("world.json",'r',encoding='utf-8-sig').read(), style_function=lambda x=None: {"fillcolour": "yellow"}))

#Puting MARKERS in map
map.add_child(fg)
map.add_child(fg2)
map.add_child(folium.LayerControl())
map.save('Map2.html')

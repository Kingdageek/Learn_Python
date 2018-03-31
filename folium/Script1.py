import folium
import pandas as pd

df= pd.read_csv("Volcanoes_USA.txt")
map = folium.Map(location=[df["LAT"].mean(), df["LON"].mean()], zoom_start=10, tiles= "Stamen Terrain")

min = int(min(df["ELEV"]))
#step = int((max(df["ELEV"]) - min(df["ELEV"]))/3)
def color(elev):
    if elev in range(min,min+1368):
        return "yellow"
    elif elev in range(min+1368,min+1368*2):
        return "orange"
    else:
        return "red"

for lat, lon, name, elev in zip(df["LAT"], df["LON"], df["NAME"], df["ELEV"]):
    folium.Marker([lat,lon], popup= name, icon= folium.Icon(color= color(elev), icon= "info-sign")).add_to(map)

map.save("test1.html")

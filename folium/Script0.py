import folium
map = folium.Map(location= [6.550723, 3.3067225], tiles= "OpenStreetMap", zoom_start= 12, max_zoom= 24)
folium.Marker([6.550700231, 3.30672], popup= "First Bank Ejigbo", icon= folium.Icon(color="red", icon= "info-sign")).add_to(map)
folium.Marker([6.55070023, 3.306722953], popup= "Watchman").add_to(map)

map.save("test.html")

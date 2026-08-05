import pandas as pd
import folium

df=pd.DataFrame({
    'lon':[-58,2,145,30.32,-4.03,-73.57,36.82,-38.5],
    'lat':[-34,49,-38,59.93,5.33,45.52,-1.29,-12.97],
    'name':['India','Afghanistan','England','New Zeland','Pakistan','Dubai','Shri Lanka','Nepal'],
    'value':[10,12,40,70,23,43,100,43]
},dtype=str)
df
m=folium.Map(location=[20,0],titels='Open',zoom_start=2)
m

from geopy.geocoders import OpenCage
import pandas as pd
import os


path="./donnees_geographique_agence_gab (1).xlsx"
export="."

def getLocator():
    api_key = '15460cbef5dc4477a60d07c099f63947'

    # Initialisation du géocodeur OpenCage
    geolocator = OpenCage(api_key=api_key)
    return geolocator


def get_coordinates_from_pluscode(geolocator, pluscode):
    # Utilisation du géocodeur pour obtenir la position du plus-code
    location = geolocator.geocode(pluscode)
    return location

def transform(df):
    locator= getLocator()
    print(df.columns)
    if 'Localisation_maps' in df.columns:
        for val in df['Localisation_maps'].values:
            print('Ok')
            location = get_coordinates_from_pluscode(locator,val)
            if location:
                df.loc[df['Localisation_maps']== val,"Longitude_map"]=location.longitude
                df.loc[df['Localisation_maps']== val,"Latitude_map"]=location.latitude
    return df
    
"""df=pd.read_excel(path)
df.rename(columns={'Longitude map ':'Longitude_map','Latitude map':'Latitude_map'},inplace=True)
print(df.columns)
for val in df['Localisation maps'].values:
    location = get_coordinates_from_pluscode(locator,val)
    if location:
        df.loc[df['Localisation maps']== val,"Longitude_map"]=location.longitude
        df.loc[df['Localisation maps']== val,"Latitude_map"]=location.latitude

df.to_excel(os.path.join(export,"donnees_geographique_agence_gab_traité.xlsx"))"""

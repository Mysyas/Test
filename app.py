import streamlit as st
import pandas as pd
from Geo import transform
from io import BytesIO

def to_excel(df):
    output = BytesIO()
    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="Sheet1")
    return output.getvalue()

st.set_page_config(page_title='transformateur')

st.markdown('<h1>Convertisseur Adresse en coordonnée</h1>',unsafe_allow_html=True)
loader=st.file_uploader(label='Charger le fichier')
if loader:
    df=pd.read_excel(loader, engine='openpyxl')
    cols=df.columns
    df.rename(columns={col:col.strip().replace(' ','_') for col in cols},inplace=True)
    df=transform(df)
    st.write(loader.name)
    st.download_button(
        label="Télécharger le résultat",
        data=to_excel(df),
        file_name=loader.name,
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    st.write(df)
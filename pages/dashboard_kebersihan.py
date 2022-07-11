import streamlit as st
from streamlit_echarts import st_echarts 
from plot import Pie
from data import Data

# st.set_page_config(layout="wide")

kebersihan = Data.get_data_kebersihan()

col1, col2 , col3 = st.columns(3)

with col1:
    item_kebersihan = st.selectbox("Item Kebersihan", ["Hidran", "Penampung Air", "Mata Air", "Pengelola Air", "Sumur Gali", "Sumur Pompa", "Tangki Air"])

with col2:
    filter_by_kabupaten = st.selectbox("Filter By", ["All (Provinsi)", "Kabupaten Bantul", "Kabupaten Kulon Progo", "Kabupaten Sleman", "Kabupaten Gunung Kidul"])

with col3:

    # subcol1, subcol2 = st.columns(2)
    kab = filter_by_kabupaten if filter_by_kabupaten != "All (Provinsi)" else None
    if kab != None:
        list_kecamatan = list(kebersihan.query("kotaNama == '{}'".format(filter_by_kabupaten))["kecNama"].unique())
        list_kecamatan.append("All (Kecamatan)")
        filter_by_kecamatan = st.selectbox("Kecamatan", list_kecamatan[::-1])
    
    submit= st.button("Submit") 

# data_kecamatan = list_kecamatan

if submit:
    if item_kebersihan == "Hidran":
        if kab == None:
            data_kebersihan = kebersihan.query('proNama == "Daerah Istimewa Yogyakarta"').groupby("skHidran").count()["proNama"].to_dict()
        elif filter_by_kecamatan != "All (Kecamatan)":
            data_kebersihan = kebersihan.query('(proNama == "Daerah Istimewa Yogyakarta") & (kotaNama == "{}") & (kecNama == "{}")'.format(kab, filter_by_kecamatan)).groupby("skHidran").count()["proNama"].to_dict()
        else:
            data_kebersihan = kebersihan.query('(proNama == "Daerah Istimewa Yogyakarta") & (kotaNama == "{}")'.format(kab)).groupby("skHidran").count()["proNama"].to_dict()

        # st.write(kebersihan)

    elif item_kebersihan == "Penampung Air":
        if kab == None:
            data_kebersihan = kebersihan.query('proNama == "Daerah Istimewa Yogyakarta"').groupby("skPenampung").count()["proNama"].to_dict()
        elif filter_by_kecamatan != "All (Kecamatan)":
            data_kebersihan = kebersihan.query('(proNama == "Daerah Istimewa Yogyakarta") & (kotaNama == "{}") & (kecNama == "{}")'.format(kab, filter_by_kecamatan)).groupby("skPenampung").count()["proNama"].to_dict()
        else:
            data_kebersihan = kebersihan.query('(proNama == "Daerah Istimewa Yogyakarta") & (kotaNama == "{}")'.format(kab)).groupby("skPenampung").count()["proNama"].to_dict()
   
    # data_kebersihan = kebersihan.query('proNama == "Daerah Istimewa Yogyakarta"').groupby("skHidran").count()["proNama"].to_dict()
    response_data = [{"value": data_kebersihan[i], "name":i} for i in data_kebersihan.keys()]

    option = Pie(title="Kebersihan", data=response_data, legend=True).plot()

    st_echarts(option)

st.markdown("### Raw Data")
st.write(kebersihan)
import streamlit as st
from streamlit_echarts import st_echarts

from data import Data
from plot import Line, Pie, Bar
import pandas as pd

def base_section():
    st. set_page_config(layout="wide")

    st.title("Beranda")
    
    jumlah_desa = Data.get_data_jumlah_desa()
    total_menunggu_persetujuan = Data.get_data_total_menunggu_approval().loc[0][0]
    total_disetujui = Data.get_data_total_disetujui().loc[0][0]
    total_ditolak = Data.get_data_total_ditolak().loc[0][0]

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Jumlah Desa", jumlah_desa)

    with col2:
        st.metric("Total Menunggu Persetujuan", total_menunggu_persetujuan)

    with col3:
        st.metric("Total Disetujui", total_disetujui)

    with col4:
        st.metric("Total Ditolak", total_ditolak)


    df_keaktifan = Data.get_data_keaktifan()

    teraktif = df_keaktifan.sort_values("persen", ascending=False).head(10)
    terpasif = df_keaktifan.sort_values("persen").head(10)

    col_bar1, col_bar2 = st.columns(2)

    with col_bar1:
        option_teraktif = Bar("Desa Teraktif", teraktif["kelurahan"].tolist()[::-1],[ teraktif["persen"].tolist()[::-1]],
                ["Persentase Keterisian data"], orientation="vertical").plot()

        st_echarts(options=option_teraktif)
    with col_bar2:
        option_terpasif= Bar("Desa Terpasif", terpasif["kelurahan"].tolist()[::-1],[ terpasif["persen"].tolist()[::-1]],
                ["Persentase Keterisian data"], orientation="vertical").plot()
        
        st_echarts(options=option_terpasif)


    tren_pengajuan = Data.get_data_update_harian()
    tren_pengajuan["DATE(pTgl)"] = tren_pengajuan["DATE(pTgl)"].astype(str)
    option_tren_pengajuan = Line("Update Harian", tren_pengajuan["DATE(pTgl)"].tolist(),[ tren_pengajuan["COUNT(*)"].tolist()],
                ["Update Harian"], area=True).plot()

    option_tren_pengajuan['color'] = 'red'
    st_echarts(options=option_tren_pengajuan)


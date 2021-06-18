
import streamlit as st
import imageio
import numpy as np


def normalise_data(volume, min_intensity = -1000, max_intensity = 200):
    volume = np.clip(volume, min_intensity, max_intensity)
    volume = (255*((volume - min_intensity)/(max_intensity - min_intensity))).astype(np.uint8)
    return volume
  

def display_ct_scan_interface(ct_scan):
    """
        Show a CT scan section dependending on user options
    """
    options = ['axial', 'coronal', 'sagittal'] 
    tranche = st.radio('tranche', options)
    

    slider_min = 0
    slider_max = ct_scan.shape[options.index(tranche)]

    section = st.slider("section of ct_scan", slider_min, slider_max-1)
    
    if tranche == 'axial':
        image = ct_scan[section]
    elif tranche == 'coronal':
        image = ct_scan[:, section, :]
    else: 
        image = ct_scan[:, :, section]

    

    image = np.array(image)
    
    st.image(image)


@st.cache(suppress_st_warning=True)
def load_ct_scan(folder):
    st.write("cache miss")
    image = imageio.volread(folder)
    
    return normalise_data(image)
    


st.title('CT scan explorer')

folder = st.text_input(label ="Give the path to a DCOM folder")

if (folder):

    ct_scan = load_ct_scan(folder)
    st.write("taille du volume", ct_scan.shape)
    display_ct_scan_interface(ct_scan)
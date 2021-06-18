
import streamlit as stp
import imageio


def display_ct_scan_interface(ct_scan):
    """
        Show a CT scan section dependending on user options
    """
    tranche = st.radio('tranche', ['axial', 'coaxial', 'etc'] )

    slider_min = 0
    slider_max = ct_scan.shape[tranche]

    section = st.slider("section of ct_scan", slider_min, slider_max-1)
    
    if tranche == 0:
        image = ct_scan[section]
    elif tranche == 1:
        image = ct_scan[:, section, :]
    else: 
        image = ct_scan[:, :, section]

    st.image(, channels="BGR")


st.title('CT scan explorer')
st.write('Please pick a folder !')
folder = st.file_uploader()

@st.cache
def load_ct_scan(folder):

    return  imageio.load(folder)


if (folder):

    ct_scan = load_ct_scan(folder)
    display_ct_scan_interface(ct_scan)
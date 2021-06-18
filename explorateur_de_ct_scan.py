
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

    #print(options.index[tranche])

    slider_min = 0
    slider_max = ct_scan.shape[options.index(tranche)]

    section = st.slider("section of ct_scan", slider_min, slider_max-1)
    
    if tranche == 'axial':
        image = ct_scan[section]
    elif tranche == 'coronal':
        image = ct_scan[:, section, :]
    else: 
        image = ct_scan[:, :, section]

    print("type of image", type(image))

    image = np.array(image)
    image = normalise_data(image)

    st.image(image)





st.title('CT scan explorer')
#st.write('Please pick a folder !')
folder = st.file_uploader(label =" Please pick a folder", accept_multiple_files=True)
folder = "/Users/bnmac/Documents/Nowledgable/MonAi/ct_scan/train/ID00180637202240177410333"

print('folder', folder)

@st.cache
def load_ct_scan(folder):
    image = imageio.volread(folder)
    print("image shape", image.shape )
    return image


if (folder):

    ct_scan = load_ct_scan(folder)
    display_ct_scan_interface(ct_scan)
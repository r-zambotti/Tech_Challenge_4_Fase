import streamlit as st

import warnings
warnings.filterwarnings('ignore')
## ----------------------------------------- ##
##                 Streamlit                 ##
## ----------------------------------------- ##
def insert_image(image_path, caption, source=None, width=600) -> None:
    '''
    Insert image in the streamlit app.
    
    Parameters:
    image_path: str, path to the image.
    caption: str, caption of the image.
    source: str, source of the image.
    width: int, width of the image. Default is 600.
    
    Returns:
    None
    '''

    st.image(image_path, width=width)
    # legenda
    if source is None:
        st.markdown(f'<p style=font-size: 12px">{caption}</p>', unsafe_allow_html=True)
    else:
        st.markdown(f'<p style=font-size: 12px">{caption} | <a href="{source}" target="_blank">[Link]</a></p>', unsafe_allow_html=True)
    

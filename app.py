import streamlit as st
import cv2
import numpy as np
from measurements import get_body_measurements, get_skin_color
from size_config import BRAND_DATA

st.set_page_config(page_title="AI Fashion Stylist", layout="wide")
st.title("👗 AI Fashion Stylist & Size Recommender")

# Sidebar settings (Slider khatam kar dia ha)
brand = st.sidebar.selectbox("Select Brand", list(BRAND_DATA.keys()))
run = st.checkbox('Start Camera')

# Fixed Calibration Ratio (Slider ki jagah hardcoded value)
# Aap isay 0.04 se 0.05 ke darmiyan set kar saktay hain
RATIO = 0.045 

col1, col2 = st.columns([2, 1])

with col1:
    FRAME_WINDOW = st.image([])

with col2:
    st.subheader("Live Analysis")
    res_text = st.empty()
    size_text = st.empty()
    color_info = st.empty()
    color_list = st.empty()

camera = cv2.VideoCapture(0)

while run:
    ret, frame = camera.read()
    if not ret: break
    frame = cv2.flip(frame, 1)
    
    # RATIO variable pass ho rha ha slider ki jagah
    chest, waist, landmarks = get_body_measurements(frame, RATIO)
    
    if chest:
        recommended_size = "Not Found"
        for size, limits in BRAND_DATA[brand].items():
            c_min, c_max = limits['chest']
            if c_min <= chest <= c_max:
                recommended_size = size
                break
        
        skin_type, colors = get_skin_color(frame, landmarks)
        
        # Immediate Results display
        res_text.markdown(f"**Chest:** {chest} in | **Waist:** {waist} in")
        size_text.success(f"Recommended {brand} Size: **{recommended_size}**")
        color_info.info(f"Detected Skin Tone: **{skin_type}**")
        color_list.write(f"Best Colors for you: **{', '.join(colors)}**")
        
    FRAME_WINDOW.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
else:
    camera.release()
    st.write('Camera is Stopped')
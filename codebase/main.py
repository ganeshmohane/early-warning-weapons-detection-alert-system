import os
import cv2
import time
import numpy as np
import streamlit as st
from core import data_processing as dp
from core import model_detection as md
from core import threat_analysis as ta
from core import send_alert as sa


st.title('Early Warning Weapons Detection & Alert System')

uploaded_file =  st.file_uploader(label="Choose A Image/Video For Detection", type=['mp4', 'mov', 'avi', 'jpg', 'png'])
if uploaded_file is not None:

    file_type = uploaded_file.type

    if file_type in ['video/mp4','video/mov', 'video/avi']:
        video_placeholder = st.empty()
        st.video(uploaded_file)
    if file_type in ['image/jpeg', 'image/png']:
        st.image(uploaded_file)


    if st.button('Run Real Time Detection'):

        # Video files
        if file_type in ['video/mp4','video/mov','video/avi']:
            frames, video_path = dp.process_video(uploaded_file)

            video_placeholder = st.empty()

            alert_sent = False 

            for frame_id, frame in frames:
                # YOLO detection
                detected_weapon, accuracy, boxed_frame = md.detect_weapons(frame)
                boxed_frame = cv2.cvtColor(boxed_frame, cv2.COLOR_BGR2RGB)
                video_placeholder.image(boxed_frame, caption=f"Frame {frame_id} - {detected_weapon} ({accuracy}%)",  width='content')
                
                # email alert
                if not alert_sent and detected_weapon not in ['no_weapon', None]:
                    data = ta.detect_threat_level(boxed_frame, detected_weapon.title(), accuracy)
                    alert_sent = True
                time.sleep(1.5)

            os.remove(video_path)
            st.success("Detection Complete ✅")


        # Images files  
        elif file_type in ['image/jpeg','image/png']:
            frame = dp.process_image(uploaded_file)

            detected_weapon, accuracy, boxed_frame = md.detect_weapons(frame)
            print(detected_weapon, accuracy)

            data = ta.detect_threat_level(boxed_frame, detected_weapon.title(), accuracy)

            st.image(boxed_frame, caption=f"{data['weapon']} - Threat level: {data['threat_level']}")
            st.success("Detection Complete ✅")
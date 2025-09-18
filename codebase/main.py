import streamlit as st
from core import data_processing as dp
from core import model_detection as md
from core import threat_analysis as ta
from core import send_alert as sa


st.title('🔫 Early Warning Weapons Detection & Alert System')

uploaded_file =  st.file_uploader(label="Choose A Video For Detection", type=['mp4', 'mov', 'avi', 'jpg', 'png'])

if uploaded_file is not None:

    file_type = uploaded_file.type

    if file_type in ['video/mp4','video/mov', 'video/avi']:
        st.video(uploaded_file)
    if file_type in ['image/jpeg', 'image/png']:
        st.image(uploaded_file)



    if st.button('Run Detection'):
        # send video to data_processing.py
        # run model on each frame
        # send result to threat_analysis.py
        # show live detected frames one ready, all thid do in live & alert by adding alert and sending whastapp.call msg with captured suspect image & location

        location = 'Sector 1, Navi Mumbai'
        if file_type in ['video/mp4','video/mov','video/avi']:
            frames = dp.process_video(uploaded_file)

            for frame_id, frame in frames:
                detected_weapon, accuracy = md.detect_weapons(frame)
                data = ta.detect_threat_level(frame, detected_weapon, accuracy)
                
                #st.image(frame, caption=f"Frame {frame_id} - {detected_weapon} ({accuracy}%)")

        elif file_type in ['image/jpeg','image/png']:
            frame = dp.process_image(uploaded_file)

            detected_weapon, accuracy = md.detect_weapons(frame)
            data = ta.detect_threat_level(frame, detected_weapon, accuracy)

           #st.image(frame, caption=f"{detected_weapon} ({accuracy}%)")

        data = ta.detect_threat_level(frame, detected_weapon, accuracy)
        image = data.get('image')
        weapon = data.get('weapon')
        threat_level = data.get('threat_level') 
        accuracy = data.get('accuracy')

        #st.write(sa.alert_police(image, location, threat_level))

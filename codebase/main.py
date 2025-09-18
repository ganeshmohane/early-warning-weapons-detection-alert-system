import streamlit as st
import data_processing as dp
import threat_analysis as ta
import send_alert as sa


st.title('🔫 Early Warning Weapons Detection & Alert System')

uploaded_file =  st.file_uploader(label="Choose A Video For Detection", type=['mp4'])

if uploaded_file is not None:
    st.video(uploaded_file)
    st.write('____Details_____')
    st.write(uploaded_file.name)
    st.write(uploaded_file.type)

    # send video to data_processing.py
    # run model on each frame
    # send result to threat_analysis.py
    # show live detected frames one ready, all thid do in live & alert by adding alert and sending whastapp.call msg with captured suspect image & location

    location = 'Sector 1, Navi Mumbai'

    frame, detected_weapon, accuracy = 'image_6789', 'gun', 92 #dp.process_video/image(uploaded_file)

    data = ta.threat_analysis(frame, detected_weapon, accuracy)
    image = data.get('image')
    weapon = data.get('weapon')
    threat_level = data.get('threat_level') 
    accuracy = data.get('accuracy')

    print('after threat_analysis:', image, weapon, threat_level, accuracy)

    st.write(sa.send_alert(image, location, threat_level))

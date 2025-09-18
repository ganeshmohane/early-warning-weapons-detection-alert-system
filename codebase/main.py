import streamlit as st

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
    # show live detected frames one ready, all thid do in live & alert by adding alert and sending whastapp.call msg
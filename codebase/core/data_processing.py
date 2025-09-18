import cv2
import tempfile
import os
import numpy as np

def process_video(uploaded_file, frame_skip=30):
    # Save uploaded file to a temporary location
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_path = tfile.name

    cap = cv2.VideoCapture(video_path)
    frames = []
    frame_id = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Grab every Nth frame
        if frame_id % frame_skip == 0:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append((frame_id, frame_rgb))

        frame_id += 1

    cap.release()
    os.remove(video_path)
    return frames


def process_image(uploaded_file):
    file_bytes = uploaded_file.read()
    np_arr = np.frombuffer(file_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb

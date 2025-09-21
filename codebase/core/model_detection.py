import os
import numpy as np
from dotenv import load_dotenv
from ultralytics import YOLO
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "best.pt") #yolov8n.pt

model = YOLO(MODEL_PATH)


np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(model.names), 3), dtype=np.uint8)

def detect_weapons(frame):
    """
    Run YOLOv8 on a single frame and return weapon + accuracy.
    """
    results = model.predict(frame, verbose=False)

    detected_weapon = 'no_weapon'
    accuracy = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0]) * 100
            label = model.names[cls_id].lower()

            detected_weapon = label
            accuracy = round(conf, 2)

            color = tuple(int(c) for c in colors[cls_id])

            # Get box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # xyxy coordinates
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(
                frame,
                f"{label} {accuracy:.1f}%",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                color,
                2
            )

    return detected_weapon, accuracy, frame

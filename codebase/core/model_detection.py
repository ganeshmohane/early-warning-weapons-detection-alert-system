from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_weapons(frame):
    """
    Run YOLOv8 on a single frame and return weapon + accuracy.
    """
    results = model.predict(frame, verbose=False)
    
    # Default return
    detected_weapon = "no_weapon"
    accuracy = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0]) * 100
            label = model.names[cls_id].lower()

            if label in ["gun", "knife", "improvised_weapon"]:
                detected_weapon = label
                accuracy = round(conf, 2)
                break

    return detected_weapon, accuracy


def apply_genai_layer(frame):
    pass
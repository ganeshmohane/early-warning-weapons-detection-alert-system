import os
from ultralytics import YOLO
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "yolov8n.pt")

model = YOLO(MODEL_PATH)

def detect_weapons(frame):
    """
    Run YOLOv8 on a single frame and return weapon + accuracy.
    """
    results = model.predict(frame, verbose=False)

    detected_weapon = ''
    accuracy = 0

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0]) * 100
            label = model.names[cls_id].lower()

            # if label in ["gun", "knife", "improvised_weapon", "no_weapon"]:  #['no_weapon', 'handgun', 'pistol', 'shotgun', 'rifle', 'knife', 'improvised_weapon']
            #    detected_weapon = label
            #    accuracy = round(conf, 2)
            #    break

            detected_weapon = label
            accuracy = round(conf, 2)

            # Get box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # xyxy coordinates
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  # Red box
            cv2.putText(frame, f"{label} {accuracy:.1f}%", (x1, y1-10),
            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    return detected_weapon, accuracy, frame


def apply_genai_layer(frame):
    '''
    This will take image that is skipped as no_weapon found, and another who found means it is a compulsory filter. 
    Now this genai_layer will try to identify the improvised weapon in no_weapon, And in image where weapon found it will try to understand the background context.
    Based on that it will give final result dictinary
    {
        'image': frame,
        'weapon': weapon_name,
        'accuracy': accuracy_score,
        'genai_weapon': 'yes/no',
        'genai_weapon_category': '',
        'evidence_by_genai': 'because the background image is kitchen'
    } 

    Save the frame that is flagged as weapon in folder and the name of that frame will be all the above details with space in between i.e. img121_gun_92_ so on.

    '''
    pass
import os
import numpy as np
from dotenv import load_dotenv
from ultralytics import YOLO
import cv2

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "yolov8n.pt")

model = YOLO(MODEL_PATH)


np.random.seed(42)
colors = np.random.randint(0, 255, size=(len(model.names), 3), dtype=np.uint8)

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


import re
import json

def parse_gemini_response(text):
    cleaned = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip(), flags=re.DOTALL)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return {
            "genai_weapon": "no",
            "genai_weapon_category": "",
            "evidence_by_genai": text
    }


from google import genai
from google.genai import types
import json
import cv2

load_dotenv()
genai_api_key = os.environ.get("GENAI_API_KEY")

def apply_genai_layer(frame, detected_weapon, gemini_api_key=genai_api_key):

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

    _, img_bytes = cv2.imencode('.jpg', frame)
    image_bytes = img_bytes.tobytes()

    prompt_text = f"""
    Analyze the image for weapons or improvised weapons.
    1. Identify weapon presence.
    2. If safe context (kitchen, doctor's hand, training knife), mark 'no'.
    3. Otherwise, mark 'yes' and categorize.
    4. Return strict JSON: {{"genai_weapon": "yes/no", "genai_weapon_category": "<category>", "evidence_by_genai": "<reasoning>"}}
    """

    client = genai.Client(api_key=gemini_api_key)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            prompt_text
        ]
    )

    try:
        result = json.loads(response.text)
    except:
        result = {
            "genai_weapon": "no",
            "genai_weapon_category": "",
            "evidence_by_genai": response.text
        }

    result = parse_gemini_response(response.text)

    result["image"] = frame
    result["weapon"] = detected_weapon
    return result


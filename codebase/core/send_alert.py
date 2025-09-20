
from io import BytesIO
from PIL import Image
import datetime
import os
from dotenv import load_dotenv
from resend import Emails
import numpy as np

load_dotenv()
resend_api_key = os.environ.get("RESEND_API_KEY")
Emails.api_key = resend_api_key


def send_alert(image, location, threat_level, detected_weapon, to_email): 

    if image.dtype != np.uint8:
        image = image.astype(np.uint8)

    pil_image = Image.fromarray(image)
    if pil_image.mode != "RGB":
        pil_image = pil_image.convert("RGB")
    pil_image = pil_image.resize((500, 500))

    buffer = BytesIO()
    pil_image.save(buffer, format="JPEG")
    buffer.seek(0)
    image_bytes = buffer.read()
    image_bytes_list = list(image_bytes)

    time_now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    subject = f"⚠️ Weapon Alert – Threat Level: {threat_level}"

    attachment = {
        "content": image_bytes_list,
        "filename": f"alert_{time_now}.jpg",
        "content_id": "suspect-image",
        "type": "image/jpeg"
    }

    html_content = f"""
    <div style="font-family: Arial; padding: 20px;">
        <h2>Weapon Alert Notification</h2>
        <p><strong>Detected Weapon:</strong> {detected_weapon}</p>
        <p><strong>Threat Level:</strong> {threat_level}</p>
        <p><strong>Location:</strong> {location}</p>
        <p><strong>Time:</strong> {time_now}</p>
        <p>The suspect image is attached and also displayed below:</p>
        <img src="cid:suspect-image" style="max-width:100%; height:auto;"/>
        <p>This is an automated alert from the Early Warning Weapons Detection System intended only for police.</p>
    </div>
    """

    return Emails.send({
        "from": "Early Warning System <alert@veloitsolutions.in>",
        "to": [to_email],
        "subject": subject,
        "html": html_content,
        "attachments": [attachment]
    })
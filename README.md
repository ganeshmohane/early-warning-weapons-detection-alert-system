<h1 align="center">Early Warning Weapons Detection and Alert System 🎦</h1>

The **Early Warning Weapons Detection and Alert System** is an AI-powered security solution designed to automatically detect firearms and other lethal weapons in real-time using CCTV cameras. Upon detection, it immediately notifies law enforcement and security personnel, allowing them to respond before any harmful incident occurs. This system provides continuous monitoring in public spaces, large gatherings, and events, ensuring proactive safety where human surveillance alone is insufficient.

## Application
- Ensuring safety at large public events, such as festivals, concerts, and markets.
- Supplementing human security efforts for 24/7 surveillance.
- Rapid identification and alerting of potential threats in crowded areas.
- Detecting improvised weapons and contextually unsafe objects in real-time.
- Reducing the risk of accidents or attacks by proactive threat detection.

## Objectives
- Detect Bad things before happens and prevent them from happening
- Prevent incidents by detecting threats before they occur.
- Keep public spaces, events, and gatherings safe.
- Automate monitoring to support security personnel.
- Provide context-aware alerts, distinguishing between safe objects (e.g., kitchen knives) and potential weapons

## TechStack
- Python
- Yolov8
- Streamlit

## Model Metrics

### [Dataset link](https://app.roboflow.com/ganesh-lbmbj/weapons-detection-xtbsk/2)
### [Kaggle Notebook](https://www.kaggle.com/code/ganeshmohane/yolov8-v3-0-weapon-detection-model)

<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/571f8ae3-4116-441c-9c62-2992d2620d52" />

- **Precision (B): 89.73%**
- Recall (B): 50.75%
- mAP@50 (B): 59.26%
- mAP@50-95 (B): 37.79%

## Screenshots of the project

- ### frontend UI
<img width="844" height="425" alt="image" src="https://github.com/user-attachments/assets/7b51f046-7eeb-4099-b318-39ac77c68c64" />

- ### Model Detections

<p align="center">
  <img src="https://github.com/user-attachments/assets/fbd759a8-edc2-4c41-ad4d-77d53a19180c" alt="Class Stats 1" width="300"/>
  <img src="https://github.com/user-attachments/assets/fef4a3c0-18e1-400e-825d-e0e00d3b6856" alt="Class Stats 2" width="300"/>
  <img src="https://github.com/user-attachments/assets/2c78a6e5-7e55-4862-ae11-2855d662e710" alt="Class Stats 3" width="300"/>
</p>
<p align="center">
  <img src="https://github.com/user-attachments/assets/cfdaf56f-0d19-4eab-ae47-027ae33a40d2" alt="Class Stats 4" width="300"/>
  <img src="https://github.com/user-attachments/assets/1f3ef455-53fc-4062-8950-3ffccd18b618" alt="Class Stats 5" width="300"/>
  <img src="https://github.com/user-attachments/assets/1edce79b-6614-4d66-ba42-c0d59d89532b" alt="Class Stats 6" width="300"/>
</p>


- ### Received Alert mail
<p align="center">
  <img src="https://github.com/user-attachments/assets/51a1709f-1ec6-41a9-91d6-62f12613db8d" alt="Class Stats 1" width="300" />
  <img src="https://github.com/user-attachments/assets/44ae117c-9f81-4735-8e83-2e662545b1a5" alt="Class Stats 2" width="300" />
</p>



## About Context Problem
> The problem of understanding whether given weapon is safe in different context, For that we can use genai_layer which I tried in another branch - **feature/genai_layer** you can check out the logic. Also other way is if we do not want to inlcude genai is by building multiple models pipeline. for example one model is for detetction of weapons another is detection of images background so if we got weapon as kitchen and background is kitchen then we can consider it as a safe to reduce false alarms.

## Installation steps guide
> If you face any issues during installation, [contact me](mailto:ganeshmohane_ds@ltce.in).
```bash
git clone https://github.com/ganeshmohane/early-warning-weapons-detection-alert-system
```
```bash
cd codebase
```
```bash
python -m venv venv
```
```bash
venv/scripts/activate  # for windows
```
```bash
pip install uv 
```
```bash
uv pip install -r requirements.txt
```
```bash
Create .env inside codebase folder & copy paste gist data(provided with submission mail)  as it is 
```
```bash
streamlit run main.py
```


<!-- Note: To get more context of the image and to know whether given weapon is safe, for example knife in kitchen will be considered as safe. Only for thats purpose GENAI is being used, The Main predictions are done by trained model and that result and frame(image) is then passed to genai layer where we get to know about image background and  context, Another main purpose of genai to use is to know about Improvised weapons which can be anything like Shattered Glass or Metal Rod etc -->

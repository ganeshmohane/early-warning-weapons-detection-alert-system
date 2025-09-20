<p align="center">
  <strong> <h1> Early Warning Weapons Detection and Alert System </h1> </strong>
</p>

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
<img />

## Screenshots of the project
- for video demo, Open the demo folder
- frontend UI
<img />
- Model Detections
<img />
<img /> 

## Installation steps guide
> If you face any issues during installation, [contact me](mailto:ganeshmohane_ds@ltce.in).
```bash
git clone https://github.com/ganeshmohane/early-warning-weapons-detection-alert-system
```
```bash
cd codebase
```
```bash
venv/scripts/activate  # for windows
```
```bash
pip install -r requirements.txt
```
```bash
Create .env & inside copy paste gist data(provided with submission mail)  as it is 
```
```bash
streamlit run main.py
```


<!-- Note: To get more context of the image and to know whether given weapon is safe, for example knife in kitchen will be considered as safe. Only for thats purpose GENAI is being used, The Main predictions are done by trained model and that result and frame(image) is then passed to genai layer where we get to know about image background and  context, Another main purpose of genai to use is to know about Improvised weapons which can be anything like Shattered Glass or Metal Rod etc -->

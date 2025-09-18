# Early-warning-weapons-detection-alert-system
System detects the firearm or any other lethal weapon carried by any person using CCTV camera's and alerts the policy and local authorities to act before any bad incident happens.

## Project Application
- Keeping Public Areas Markets or any other events safe
- Automating Tasks as Human always can keep on eye

## Project Objectives
- Detect Bad things before happens and prevent them from happening
- Keep people Safe

##  TechStack & Weapon detection accuracy metrics
- Python
- Yolov8
- Streamlit

## Screenshots of the project
- for demo video open demo folder

## Installation guide
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
Create .env 
**Note: To get more context of the image and to know wether given weapon is safe, for example knife in kitchen will be considered as safe. Only for thats purpose GENAI is being used, The Main predictions are done by trained model and that result and frame(image) is then passed to genai layer where we get to know about image background and  context, Another main purpose of genai to use is to know about Improvised weapons which can be anything like Shattered Glass or Metal Rod etc**
```
```bash
streamlit run main.py
```

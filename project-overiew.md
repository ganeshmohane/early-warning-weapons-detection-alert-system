## Project Overview
You are tasked with developing a computer vision system for security applications that can detect dangerous weapons in real-time surveillance footage. This system will help enhance public safety by identifying potential security threats before incidents occur.
Target Weapons for Detection.

```bash
Project Discussion: 

- Continous video stream will be monitored by CCTV(or other device), one frame by frame will be extracted and sent for threat_analysis.
- If Exceeds designated threat level, police authorities will be contacted immediatly with pre-recorded call and location and live image sent to whatsapp
- Can use GenAI models to verify for improvised weapons and check context for each weapon i.e. kithen knife vs knife in public spaces

```

## Your system must be capable of identifying the following weapons:

### Primary Weapon Classes (Required):
- Firearms - Handguns, pistols, rifles
- No Weapon - Normal/safe scenarios for comparison

### Advanced Categories (Bonus Points):
- Improvised Weapons - Broken bottles, metal rods
- The system should distinguish between actual weapons and similar-looking harmless objects (e.g., toy guns, kitchen utensils in appropriate contexts) to minimize false alarms in security applications.

## Core Requirements:
- Data Processing Module: Handle video input and frame extraction
- Model Implementation: Deep learning model for weapon classification
- Video Analysis Pipeline: Process video files and generate threat detection results

## Documentation Requirements
- Readme.md Must Include:
- Project description and security application objectives
- Weapon detection accuracy metrics
- Screenshots of project
- Installation and running scripts

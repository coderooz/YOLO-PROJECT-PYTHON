# YOLO Emotion Detection

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Face-green.svg)](https://docs.ultralytics.com/)

Real-time facial emotion recognition combining YOLOv8 face detection with FER emotion analysis.

## Features

- Face detection via YOLOv8-face
- Emotion classification via FER (CNN-based)
- Detects: angry, disgust, fear, happy, sad, surprise, neutral
- Live emotion labels on detected faces
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python emotion_detect.py
```

## How It Works

1. YOLOv8-face detects faces in each frame
2. Each face crop is passed to FER emotion detector
3. Top emotion is displayed above each face
4. Bounding boxes drawn around detected faces

## Models Required

Place in `../models/`:
- `yolov8n-face.pt` — face detection

FER uses its own pre-trained CNN (downloaded automatically).

## Controls

| Key | Action |
|-----|--------|
| ESC | Quit |

## Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8-face
- FER (Facial Expression Recognition)
- NumPy

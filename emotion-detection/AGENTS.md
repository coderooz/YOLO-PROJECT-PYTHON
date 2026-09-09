# emotion-detection — Agent Instructions

## Project Overview
Facial emotion recognition combining YOLOv8 face detection with FER emotion analysis. Detects faces and classifies emotions (angry, disgust, fear, happy, sad, surprise, neutral).

## Commands
- `python emotion_detect.py` — run emotion detection
- `python -m py_compile emotion_detect.py` — validate syntax
- `ruff check .` — lint

## Models Required
Place `yolov8n-face.pt` in `../models/` directory. FER downloads its own CNN automatically.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for face detection
- FER for emotion classification
- ESC key to exit

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

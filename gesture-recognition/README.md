# YOLO Gesture Recognition

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Pose-green.svg)](https://docs.ultralytics.com/)

Real-time hand gesture classification using YOLOv8 pose detection.

## Status

**Planned** — This sub-project is not yet implemented.

## Planned Features

- Hand detection with YOLOv8-pose
- Gesture classification (thumbs up, victory, stop, etc.)
- Live gesture labels
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python gesture_recognition.py
```

## Model Required

Place `yolov8n-pose.pt` in `../models/`:

```bash
# https://docs.ultralytics.com/models/yolov8/
```

## Controls

| Key | Action |
|-----|--------|
| ESC | Quit |

## Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8-pose
- NumPy

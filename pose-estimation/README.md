# YOLO Pose Estimation

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Pose-green.svg)](https://docs.ultralytics.com/)

Real-time human pose estimation with action classification using YOLOv8-pose.

## Features

- 17-keypoint pose detection
- Action classification (Hi, Hands Up)
- Live FPS display
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python pose-estimation.py
```

## Model Required

Place `yolov8n-pose.pt` in `../models/`:

```bash
# Download from Ultralytics
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

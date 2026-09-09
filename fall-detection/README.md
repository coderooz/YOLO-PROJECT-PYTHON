# YOLO Fall Detection

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Pose-green.svg)](https://docs.ultralytics.com/)

Real-time fall event detection using YOLOv8 pose estimation.

## Status

**Planned** — This sub-project is not yet implemented.

## Planned Features

- Person detection with YOLOv8
- Pose estimation for fall analysis
- Fall event detection (standing → lying)
- Alert system
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python fall_detection.py
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

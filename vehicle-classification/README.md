# YOLO Vehicle Classification

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-green.svg)](https://docs.ultralytics.com/)

Real-time vehicle type classification and tracking.

## Status

**Planned** — This sub-project is not yet implemented.

## Planned Features

- Vehicle detection with YOLOv8
- Type classification (car, motorcycle, bus, truck)
- Multi-object tracking
- Live count by type
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python vehicle_classify.py
```

## Model Required

Place `yolov8n.pt` in `../models/` (or custom-trained vehicle model):

```bash
# https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt
```

## Controls

| Key | Action |
|-----|--------|
| ESC | Quit |

## Tech Stack

- Python 3.10+
- OpenCV
- Ultralytics YOLOv8
- NumPy

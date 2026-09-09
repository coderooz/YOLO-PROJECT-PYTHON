# YOLO Crowd Counting

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-green.svg)](https://docs.ultralytics.com/)

Real-time crowd density estimation using YOLOv8 detection with tracking.

## Status

**Planned** — This sub-project is not yet implemented.

## Planned Features

- Person detection with YOLOv8
- Multi-object tracking
- Crowd density estimation
- Live count display
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python crowd_counter.py
```

## Model Required

Place `yolov8n.pt` in `../models/`:

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

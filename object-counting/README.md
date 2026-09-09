# YOLO Object Counting

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-green.svg)](https://docs.ultralytics.com/)

Real-time object counting using YOLOv8 detection with SORT tracking.

## Features

- Object detection + multi-object tracking
- SORT (Simple Online and Realtime Tracking) with Kalman filter
- Crossing-line counting
- Live count display
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python object_counter.py
```

## How It Works

1. YOLOv8 detects objects in each frame
2. SORT tracker assigns unique IDs to each object
3. Objects are counted when they cross a horizontal line
4. Count is displayed on-screen

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
- filterpy (Kalman filter)
- scipy (Hungarian algorithm)
- NumPy

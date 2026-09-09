# YOLO License Plate Detection

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-green.svg)](https://docs.ultralytics.com/)

Real-time vehicle license plate detection with OCR.

## Status

**Planned** — This sub-project is not yet implemented.

## Planned Features

- License plate detection with YOLOv8
- OCR text extraction (EasyOCR/Tesseract)
- Live plate number display
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python license_plate_detect.py
```

## Model Required

Place `yolov8n.pt` in `../models/` (or custom-trained plate model):

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
- EasyOCR / Tesseract
- NumPy

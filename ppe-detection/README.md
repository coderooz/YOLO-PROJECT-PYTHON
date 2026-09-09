# YOLO PPE Detection

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Detection-green.svg)](https://docs.ultralytics.com/)

Real-time Personal Protective Equipment (PPE) detection for workplace safety.

## Status

**Planned** — This sub-project is not yet implemented.

## Planned Features

- Helmet detection
- Vest detection
- Boots detection
- Safety compliance alerts
- Webcam inference

## Quick Start

```bash
pip install -r requirements.txt
python ppe_detect.py
```

## Model Required

Place custom PPE model in `../models/`:

```bash
# Train on PPE dataset or use pre-trained model
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

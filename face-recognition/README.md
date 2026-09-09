# YOLO Face Recognition

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![InsightFace](https://img.shields.io/badge/InsightFace-Buffalo-green.svg)](https://github.com/deepinsight/insightface)

Real-time face identification using InsightFace with Buffalo_L model.

## Features

- Face detection + recognition in one pipeline
- 512-dimensional face embeddings
- Real-time webcam inference
- Bounding box visualization

## Quick Start

```bash
pip install -r requirements.txt
python simple_face_recognition.py
```

## How It Works

1. InsightFace Buffalo_L model detects faces
2. Each face is encoded into a 512-d embedding
3. Bounding boxes drawn around detected faces
4. Ready for identity matching (extend with your own database)

## Models Required

InsightFace downloads `buffalo_l` automatically on first run.

## Controls

| Key | Action |
|-----|--------|
| ESC | Quit |

## Tech Stack

- Python 3.10+
- OpenCV
- InsightFace (Buffalo_L)
- NumPy

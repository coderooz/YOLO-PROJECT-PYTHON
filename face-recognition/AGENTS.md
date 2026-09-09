# face-recognition — Agent Instructions

## Project Overview
Face identification using InsightFace with Buffalo_L model. Real-time face detection and 512-dimensional embedding generation.

## Commands
- `python simple_face_recognition.py` — run face recognition
- `python -m py_compile simple_face_recognition.py` — validate syntax
- `ruff check .` — lint

## Models Required
InsightFace downloads `buffalo_l` automatically on first run.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- InsightFace for face detection + recognition
- ESC key to exit

## Doc References
- Python: https://docs.python.org/3/
- InsightFace: https://github.com/deepinsight/insightface

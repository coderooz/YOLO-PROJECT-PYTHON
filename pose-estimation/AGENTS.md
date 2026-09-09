# pose-estimation — Agent Instructions

## Project Overview
Human pose estimation with action classification using YOLOv8-pose. Detects 17 keypoints and classifies actions (Hi, Hands Up).

## Commands
- `python pose-estimation.py` — run pose estimation
- `python -m py_compile pose-estimation.py` — validate syntax
- `ruff check .` — lint

## Model Required
Place `yolov8n-pose.pt` in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- NumPy for keypoint processing
- ESC key to exit

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

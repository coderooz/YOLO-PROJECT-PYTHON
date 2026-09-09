# object-detection — Agent Instructions

## Project Overview
General object detection using YOLOv8. Uses YOLOv8 (Ultralytics) and OpenCV for real-time webcam inference.

## Commands
- `python object_detect.py` — run detection
- `python -m py_compile object_detect.py` — validate syntax
- `ruff check .` — lint

## Model Required
Place `yolov8n.pt` in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- ESC key to exit
- Relative model path: `../models/`

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

# object-counting — Agent Instructions

## Project Overview
Object counting using YOLOv8 detection with SORT tracking. Counts objects crossing a horizontal line using Kalman filter-based multi-object tracking.

## Commands
- `python object_counter.py` — run counter
- `python -m py_compile object_counter.py` — validate syntax
- `python -m py_compile sort.py` — validate SORT tracker
- `ruff check .` — lint

## Model Required
Place `yolov8n.pt` in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- filterpy for Kalman filter
- scipy for Hungarian algorithm
- ESC key to exit

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

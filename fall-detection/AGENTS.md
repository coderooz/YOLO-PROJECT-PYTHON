# fall-detection — Agent Instructions

## Project Overview
Fall event detection using YOLOv8 pose estimation. Planned sub-project — not yet implemented.

## Status
**Planned** — No script available yet.

## Commands (when implemented)
- `python fall_detection.py` — run fall detection
- `python -m py_compile fall_detection.py` — validate syntax
- `ruff check .` — lint

## Model Required (when implemented)
Place `yolov8n-pose.pt` in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- NumPy for keypoint processing
- ESC key to exit
- Relative model path: `../models/`

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

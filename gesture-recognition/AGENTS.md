# gesture-recognition — Agent Instructions

## Project Overview
Hand gesture classification using YOLOv8 pose detection. Planned sub-project — not yet implemented.

## Status
**Planned** — No script available yet.

## Commands (when implemented)
- `python gesture_recognition.py` — run gesture recognition
- `python -m py_compile gesture_recognition.py` — validate syntax
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

# vehicle-classification — Agent Instructions

## Project Overview
Vehicle type classification and tracking using YOLOv8. Planned sub-project — not yet implemented.

## Status
**Planned** — No script available yet.

## Commands (when implemented)
- `python vehicle_classify.py` — run vehicle classification
- `python -m py_compile vehicle_classify.py` — validate syntax
- `ruff check .` — lint

## Model Required (when implemented)
Place `yolov8n.pt` (or custom vehicle model) in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- ESC key to exit
- Relative model path: `../models/`

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

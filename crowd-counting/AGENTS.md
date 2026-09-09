# crowd-counting — Agent Instructions

## Project Overview
Crowd density estimation using YOLOv8 detection with tracking. Planned sub-project — not yet implemented.

## Status
**Planned** — No script available yet.

## Commands (when implemented)
- `python crowd_counter.py` — run crowd counter
- `python -m py_compile crowd_counter.py` — validate syntax
- `ruff check .` — lint

## Model Required (when implemented)
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

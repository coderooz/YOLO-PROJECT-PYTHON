# ppe-detection — Agent Instructions

## Project Overview
Personal Protective Equipment (PPE) detection for workplace safety. Planned sub-project — not yet implemented.

## Status
**Planned** — No script available yet.

## Commands (when implemented)
- `python ppe_detect.py` — run PPE detection
- `python -m py_compile ppe_detect.py` — validate syntax
- `ruff check .` — lint

## Model Required (when implemented)
Place custom PPE model in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- ESC key to exit
- Relative model path: `../models/`

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

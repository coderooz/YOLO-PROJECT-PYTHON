# license-plate-detection — Agent Instructions

## Project Overview
Vehicle license plate detection with OCR. Planned sub-project — not yet implemented.

## Status
**Planned** — No script available yet.

## Commands (when implemented)
- `python license_plate_detect.py` — run license plate detection
- `python -m py_compile license_plate_detect.py` — validate syntax
- `ruff check .` — lint

## Model Required (when implemented)
Place `yolov8n.pt` (or custom plate model) in `../models/` directory.

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture/display
- YOLOv8 via `ultralytics` for inference
- EasyOCR / Tesseract for text extraction
- ESC key to exit
- Relative model path: `../models/`

## Doc References
- Python: https://docs.python.org/3/
- Ultralytics: https://docs.ultralytics.com/

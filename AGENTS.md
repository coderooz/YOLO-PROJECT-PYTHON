# YOLO Projects — Agent Instructions

## Project Overview
Collection of real-time computer vision projects built with **YOLOv8** (Ultralytics) and **OpenCV**. Each sub-project demonstrates a different use-case: detection, recognition, counting, pose estimation, and emotion analysis.

## Commands
- `ruff check **/*.py` — lint all Python files
- `python -m py_compile <file>` — validate syntax
- `cd <subproject> && python <script>.py` — run sub-project

## Sub-Projects
| Sub-Project | Script | Model Required | Status |
|-------------|--------|----------------|--------|
| `face-detection/` | `face-reco.py` | `yolov8n-face.pt` | Implemented |
| `object-detection/` | `object_detect.py` | `yolov8n.pt` | Implemented |
| `pose-estimation/` | `pose-estimation.py` | `yolov8n-pose.pt` | Implemented |
| `object-counting/` | `object_counter.py` | `yolov8n.pt` | Implemented |
| `emotion-detection/` | `emotion_detect.py` | `yolov8n-face.pt` + FER | Implemented |
| `face-recognition/` | `face-recognition.py` | — | Stub |
| `crowd-counting/` | `crowd-counting.py` | — | Empty |
| `fall-detection/` | — | — | Planned |
| `gesture-recognition/` | — | — | Planned |
| `license-plate-detection/` | — | — | Planned |
| `ppe-detection/` | — | — | Planned |
| `vehicle-classification/` | — | — | Planned |

## Code Conventions
- Python 3.10+ with type hints
- OpenCV for webcam capture and display (`cv2.VideoCapture`, `cv2.imshow`)
- YOLOv8 via `ultralytics` package for inference
- Models stored in `./models/` (git-ignored, not tracked)
- Each sub-project is self-contained with its own README
- Relative model paths: `../models/<model>.pt`
- FPS displayed on-frame when applicable
- ESC key to exit all sub-projects

## Models (Not Tracked)
Model files (`*.pt`, `*.onnx`, etc.) are git-ignored. Download from:
- General: `yolov8n.pt`, `yolov8s.pt` from Ultralytics
- Face: `yolov8n-face.pt` from community sources
- Pose: `yolov8n-pose.pt` from Ultralytics
- Place in `./models/` directory

## Doc References
- Python docs: https://docs.python.org/3/
- OpenCV: https://docs.opencv.org/
- Ultralytics: https://docs.ultralytics.com/

## Project State
- Phase 1: Core detection projects implemented (face, object, pose, counting, emotion)
- Phase 2: Recognition and specialized detection (face-recognition, crowd-counting stubs)
- Phase 3: Advanced detection (fall, gesture, license-plate, PPE, vehicle) — planned

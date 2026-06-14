# YOLO Projects (Python)

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)](https://docs.ultralytics.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A collection of real-time computer vision projects built with **YOLOv8** and **OpenCV**. Each sub-project demonstrates a different use-case for YOLO in practical applications.

## Projects

| # | Sub-Project | Description | Status | Script |
|---|-------------|-------------|--------|--------|
| 1 | **Face Detection** | Real-time face detection using YOLOv8-face | Implemented | `face-detection/face-reco.py` |
| 2 | **Object Detection** | General object detection via webcam | Implemented | `object-detection/object_detect.py` |
| 3 | **Pose Estimation** | Human pose keypoint detection with action classification | Implemented | `pose-estimation/pose-estimation.py` |
| 4 | **Object Counting** | Object counting with SORT tracking | Implemented | `object-counting/object_counter.py` |
| 5 | **Emotion Detection** | Facial emotion recognition (YOLO + FER) | Implemented | `emotion-detection/emotion_detect.py` |
| 6 | **Face Recognition** | Face identification pipeline | Stub | `face-recognition/face-recognition.py` |
| 7 | **Crowd Counting** | Crowd density estimation | Planned | — |
| 8 | **Fall Detection** | Fall event detection | Planned | — |
| 9 | **Gesture Recognition** | Hand gesture classification | Planned | — |
| 10 | **License Plate Detection** | Vehicle plate recognition | Planned | — |
| 11 | **PPE Detection** | Safety equipment detection | Planned | — |
| 12 | **Vehicle Classification** | Vehicle type classification | Planned | — |

## Quick Start

```bash
# Clone
git clone https://github.com/coderooz/YOLO-PROJECT-PYTHON.git
cd YOLO-PROJECT-PYTHON

# Install dependencies
pip install -r requirements.txt

# Download models (see Models section below)
# Place in ./models/ directory

# Run a sub-project
cd face-detection
python face-reco.py
```

## Requirements

```bash
pip install -r requirements.txt
```

Core packages:
- `ultralytics` — YOLOv8 inference
- `opencv-python` — webcam capture and display
- `numpy` — array operations
- `fer` — emotion detection (for emotion-detection sub-project)

## Models

Model files are **not included** in the repository. Place downloaded models in `./models/`:

| Model | Description | Download |
|-------|-------------|----------|
| `yolov8n.pt` | General object detection (nano) | [Ultralytics](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt) |
| `yolov8s.pt` | General object detection (small) | [HuggingFace](https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8s.pt?download=true) |
| `yolov8n-face.pt` | Face detection | [Google Drive](https://drive.usercontent.google.com/u/0/uc?id=1qcr9DbgsX3ryrz2uU8w4Xm3cOrRywXqb&export=download) |
| `yolov8n-pose.pt` | Pose estimation | [Ultralytics](https://docs.ultralytics.com/models/yolov8/) |

## Repository Structure

```
YOLO-PROJECT-PYTHON/
├── face-detection/
│   ├── face-reco.py
│   └── README.md
├── object-detection/
│   ├── object_detect.py
│   └── README.md
├── pose-estimation/
│   ├── pose-estimation.py
│   └── README.md
├── object-counting/
│   ├── object_counter.py
│   ├── sort.py
│   └── README.md
├── emotion-detection/
│   ├── emotion_detect.py
│   └── README.md
├── face-recognition/
│   ├── face-recognition.py
│   ├── simple_face_recognition.py
│   └── README.md
├── crowd-counting/
│   └── README.md
├── models/                  # Git-ignored — download locally
├── image/                   # Preview screenshots
├── .opencode/               # OpenCode configuration
├── opencode.jsonc           # OpenCode project config
├── AGENTS.md                # Agent instructions
├── PROJECT_STATUS.md        # Development status
├── requirements.txt
├── LICENSE
└── README.md
```

## Tech Stack

- **Python 3.10+**
- **OpenCV** — video capture, image processing, display
- **Ultralytics YOLOv8** — object detection, face detection, pose estimation
- **FER** — facial emotion recognition (CNN-based)
- **NumPy** — numerical operations

## Usage Notes

- All sub-projects use your **webcam** (camera index 0)
- Press **ESC** to exit any sub-project
- Model files must be in `../models/` relative to each sub-project
- FPS is displayed on-screen when available

## Project Status

See [PROJECT_STATUS.md](PROJECT_STATUS.md) for detailed development progress.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.

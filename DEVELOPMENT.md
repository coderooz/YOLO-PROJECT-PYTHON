# Developer Notes — YOLO Projects (Python)

## Project Overview

A collection of real-time computer vision projects built with **YOLOv8** (Ultralytics) and **OpenCV**. Each sub-project demonstrates a different use-case for YOLO in practical applications: face detection, object detection, pose estimation, object counting, and emotion analysis.

**Repository:** [coderooz/YOLO-PROJECT-PYTHON](https://github.com/coderooz/YOLO-PROJECT-PYTHON)
**License:** MIT
**Status:** Phase 1 complete (5/12 sub-projects implemented)

---

## Architecture

### High-Level Pattern

Every implemented sub-project follows the same architecture:

```
YOLO Model (../models/*.pt)
    ↓
OpenCV VideoCapture (webcam)
    ↓
Frame → YOLO Inference
    ↓
Post-processing (boxes, keypoints, emotions)
    ↓
OpenCV Display (annotated frame + FPS)
    ↓
ESC key → Exit
```

### Major Components

| Component | Responsibility |
|-----------|---------------|
| `face-detection/` | Real-time face detection using YOLOv8-face |
| `object-detection/` | General object detection via webcam |
| `pose-estimation/` | Human pose keypoint detection with action classification |
| `object-counting/` | Object counting with SORT multi-object tracking |
| `emotion-detection/` | Facial emotion recognition (YOLO face + FER CNN) |
| `face-recognition/` | Face identification pipeline (InsightFace, stub) |
| `models/` | YOLO model files (git-ignored, downloaded separately) |

### Key Dependencies

- **Ultralytics YOLOv8** — Core detection/pose/face models
- **OpenCV** — Webcam capture, image processing, display
- **FER** — Facial emotion recognition (CNN-based, auto-downloads)
- **InsightFace** — Face recognition embeddings (auto-downloads buffalo_l)
- **filterpy** — Kalman filter for SORT tracker
- **scipy** — Hungarian algorithm for SORT tracker
- **NumPy** — Numerical operations

---

## Repository Structure

```
YOLO-PROJECT-PYTHON/
├── face-detection/          # IMPLEMENTED — face-reco.py
├── object-detection/        # IMPLEMENTED — object_detect.py
├── pose-estimation/         # IMPLEMENTED — pose-estimation.py
├── object-counting/         # IMPLEMENTED — object_counter.py + sort.py
├── emotion-detection/       # IMPLEMENTED — emotion_detect.py
├── face-recognition/        # STUB — simple_face_recognition.py
├── crowd-counting/          # PLANNED
├── fall-detection/          # PLANNED
├── gesture-recognition/     # PLANNED
├── license-plate-detection/ # PLANNED
├── ppe-detection/           # PLANNED
├── vehicle-classification/  # PLANNED
├── models/                  # Git-ignored — download models here
├── image/                   # Preview screenshots
├── .github/                 # CI workflows, templates, CODEOWNERS
├── .opencode/               # OpenCode agent config + PRI
├── AGENTS.md                # AI agent instructions
├── CHANGELOG.md             # Version history
├── CONTRIBUTING.md          # Contribution guidelines
├── DEVELOPMENT.md           # This file (developer notes)
├── LICENSE                  # MIT License
├── PROJECT_STATUS.md        # Development progress tracker
├── README.md                # Main project documentation
├── opencode.jsonc           # OpenCode project configuration
└── requirements.txt         # Python dependencies
```

---

## Development Environment

### Required Runtime

- **Python:** 3.10 or later
- **OS:** Windows, macOS, or Linux (developed on Windows)
- **Webcam:** Required for all sub-projects (camera index 0)

### Required Tools

- `pip` — Python package manager
- `ruff` — Python linter (for code quality checks)

### Setup

```bash
# Clone the repository
git clone https://github.com/coderooz/YOLO-PROJECT-PYTHON.git
cd YOLO-PROJECT-PYTHON

# Create virtual environment
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/Mac:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install dev tools (optional)
pip install ruff
```

### Model Files

Model files are **not included** in the repository. Download and place in `./models/`:

| Model | Purpose | Source |
|-------|---------|--------|
| `yolov8n.pt` | General object detection | [Ultralytics](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt) |
| `yolov8n-face.pt` | Face detection | [Google Drive](https://drive.usercontent.google.com/u/0/uc?id=1qcr9DbgsX3ryrz2uU8w4Xm3cOrRywXqb&export=download) |
| `yolov8n-pose.pt` | Pose estimation | [Ultralytics](https://docs.ultralytics.com/models/yolov8/) |

FER and InsightFace models download automatically on first run.

---

## Running the Project

### Run a Sub-Project

```bash
cd face-detection
python face-reco.py
```

### Available Sub-Projects

| Command | Description |
|---------|-------------|
| `cd face-detection && python face-reco.py` | Face detection |
| `cd object-detection && python object_detect.py` | Object detection |
| `cd pose-estimation && python pose-estimation.py` | Pose estimation |
| `cd object-counting && python object_counter.py` | Object counting |
| `cd emotion-detection && python emotion_detect.py` | Emotion detection |
| `cd face-recognition && python simple_face_recognition.py` | Face recognition (stub) |

### Controls

All sub-projects use **ESC** to exit.

---

## Testing

### Syntax Validation

```bash
python -m py_compile face-detection/face-reco.py
python -m py_compile object-detection/object_detect.py
python -m py_compile pose-estimation/pose-estimation.py
python -m py_compile object-counting/object_counter.py
python -m py_compile object-counting/sort.py
python -m py_compile emotion-detection/emotion_detect.py
python -m py_compile face-recognition/simple_face_recognition.py
```

### Linting

```bash
ruff check .
```

### CI Pipeline

GitHub Actions runs automatically on push/PR to `main`:
- Lint with ruff
- Syntax validation for all implemented scripts
- Tests across Python 3.10, 3.11, 3.12

---

## Maintenance

### Adding a New Sub-Project

1. Create directory: `your-project/`
2. Add Python script(s)
3. Add `README.md` with description, model requirements, usage
4. Add `AGENTS.md` with agent instructions
5. Update root `README.md` project table
6. Update root `AGENTS.md` sub-projects table
7. Update `PROJECT_STATUS.md`

### Common Tasks

- **Update dependencies:** Edit `requirements.txt`, test all sub-projects
- **Add model support:** Update `README.md` download table, test inference
- **Fix a bug:** Fix in the sub-project script, validate with `py_compile`

### Project Logic

- All detection logic lives in individual sub-project Python scripts
- SORT tracker logic is in `object-counting/sort.py`
- No shared library — each sub-project is self-contained
- Model paths are relative: `../models/<model>.pt`

---

## Known Issues

1. **Model files not in repo** — Must be downloaded manually (see README)
2. **Camera dependency** — All sub-projects require an active webcam
3. **SORT tracker** — `KalmanBoxTracker.count` never resets between runs
4. **No GPU acceleration** — CPU inference by default
5. **Single-threaded** — No async/parallel processing

---

## Preservation / Recovery

### Repository Location

- **GitHub:** https://github.com/coderooz/YOLO-PROJECT-PYTHON
- **Branch:** `main`

### Recovery Steps

```bash
git clone https://github.com/coderooz/YOLO-PROJECT-PYTHON.git
cd YOLO-PROJECT-PYTHON
python -m venv .venv
.venv\Scripts\activate  # or source .venv/bin/activate
pip install -r requirements.txt
# Download models to ./models/
# Run any sub-project
```

### External Dependencies

| Dependency | Type | Required | How to Obtain |
|------------|------|----------|---------------|
| YOLO models (.pt) | Files | Yes | Download from Ultralytics/Google Drive |
| FER CNN | Auto-download | For emotion-detection | Installed with `pip install fer` |
| InsightFace buffalo_l | Auto-download | For face-recognition | Installed with `pip install insightface` |
| Webcam | Hardware | Yes | Physical webcam required |

### Intentionally Excluded from Git

- `models/` — Large model files (10-100MB each)
- `venv/`, `.venv/` — Virtual environments
- `.vscode/` — IDE configuration
- `test/` — Project ideas reference
- `.workspace/` — Development artifacts
- `*.py[cod]` — Python bytecode

### Recovery Verification

The repository can be fully reconstructed from Git alone, provided:
1. Python 3.10+ is available
2. `pip install -r requirements.txt` succeeds
3. Model files are downloaded to `./models/`
4. A webcam is available for runtime testing

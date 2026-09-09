# Project Reference Index — YOLO Projects (Python)

> **Canonical structural reference for the YOLO Projects repository.**
> This file describes verified current structure: directories, modules, configuration, entry points, and relationships.
> PRI is NOT MCP memory — PRI = "where things are and what they do"; MCP = "why things were done and what was learned".

---

## 1. Reference Metadata

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Status** | active |
| **Created** | 2026-09-06 |
| **Last Verified** | 2026-09-09 |
| **Verification Scope** | FULL |
| **Verification Method** | Filesystem inspection + content read |

---

## 2. Project Identity

| Field | Value |
|-------|-------|
| **Name** | YOLO Projects (Python) |
| **Repository** | coderooz/YOLO-PROJECT-PYTHON |
| **Remote** | https://github.com/coderooz/YOLO-PROJECT-PYTHON.git |
| **Branch** | main |
| **Purpose** | Showcase + reference collection for YOLO usage patterns |
| **Category** | Python computer vision demo collection |
| **License** | MIT |
| **Author** | Ranit Saha (Coderooz) |

---

## 3. Technology Stack

| Layer | Technology | Version |
|-------|-----------|---------|
| Language | Python | 3.10+ |
| Detection | Ultralytics YOLOv8 | 8.0+ |
| Vision | OpenCV | 4.8+ |
| Emotion | FER | 22.5+ |
| Face Recognition | InsightFace (Buffalo_L) | 0.7.3+ |
| Tracking | SORT (custom Kalman filter) | — |
| Numerical | NumPy | 1.24+ |
| Kalman Filter | filterpy | 1.4.5+ |
| Hungarian Algorithm | scipy | 1.10+ |

---

## 4. Root Structure

```
C:\Code_Works\Python_works\Yolo\
├── .github/                    # GitHub configuration (CI, templates, CODEOWNERS)
├── .opencode/                  # OpenCode configuration (agents, skills)
├── .workspace/                 # Development artifacts (git-ignored)
├── crowd-counting/             # Crowd density estimation (PLANNED)
├── emotion-detection/          # Facial emotion recognition (IMPLEMENTED)
├── face-detection/             # Real-time face detection (IMPLEMENTED)
├── face-recognition/           # Face identification with InsightFace (STUB)
├── fall-detection/             # Fall event detection (PLANNED)
├── gesture-recognition/        # Hand gesture classification (PLANNED)
├── image/                      # Preview images for READMEs
├── license-plate-detection/    # Vehicle plate recognition (PLANNED)
├── models/                     # YOLO model files (git-ignored)
├── object-counting/            # Object counting with SORT tracking (IMPLEMENTED)
├── object-detection/           # General object detection (IMPLEMENTED)
├── ppe-detection/              # Safety equipment detection (PLANNED)
├── pose-estimation/            # Human pose estimation (IMPLEMENTED)
├── test/                       # Project ideas reference (git-ignored)
├── vehicle-classification/     # Vehicle type classification (PLANNED)
├── AGENTS.md                   # Agent instructions (root)
├── CONTRIBUTING.md             # Contribution guidelines
├── docs-repo.project-mcp.json  # MCP project configuration
├── .gitignore                  # Git exclusions
├── .mcp-runtime.json           # MCP runtime state
├── LICENSE                     # MIT License
├── opencode.jsonc              # OpenCode project configuration
├── PROJECT_STATUS.md           # Development progress tracker
├── README.md                   # Main project documentation
└── requirements.txt            # Python dependencies
```

---

## 5. Directory Reference

### Implemented Sub-Projects

| Directory | Purpose | Script | Model Required | Status |
|-----------|---------|--------|----------------|--------|
| `face-detection/` | Real-time face detection | `face-reco.py` | `yolov8n-face.pt` | Implemented |
| `object-detection/` | General object detection | `object_detect.py` | `yolov8n.pt` | Implemented |
| `pose-estimation/` | Human pose estimation + action classification | `pose-estimation.py` | `yolov8n-pose.pt` | Implemented |
| `object-counting/` | Object counting with SORT tracking | `object_counter.py` | `yolov8n.pt` | Implemented |
| `emotion-detection/` | Facial emotion recognition (YOLO + FER) | `emotion_detect.py` | `yolov8n-face.pt` + FER | Implemented |

### Stub Sub-Projects

| Directory | Purpose | Script | Status |
|-----------|---------|--------|--------|
| `face-recognition/` | Face identification with InsightFace | `simple_face_recognition.py` | Stub (basic detection only) |

### Planned Sub-Projects

| Directory | Purpose | Status |
|-----------|---------|--------|
| `crowd-counting/` | Crowd density estimation | Planned (empty) |
| `fall-detection/` | Fall event detection | Planned (empty) |
| `gesture-recognition/` | Hand gesture classification | Planned (empty) |
| `license-plate-detection/` | Vehicle plate recognition | Planned (empty) |
| `ppe-detection/` | Safety equipment detection | Planned (empty) |
| `vehicle-classification/` | Vehicle type classification | Planned (empty) |

### Supporting Directories

| Directory | Purpose | Tracked |
|-----------|---------|---------|
| `models/` | YOLO model files (.pt, .onnx) | No (git-ignored) |
| `image/` | Preview images for READMEs | Yes |
| `test/` | Project ideas reference document | No (git-ignored) |
| `.github/` | CI workflows, issue templates, PR template | Yes |
| `.opencode/` | OpenCode agent configuration | Yes |
| `.workspace/` | Development artifacts | No (git-ignored) |

---

## 6. File Reference

### Python Scripts

| File | Purpose | Lines | Imports |
|------|---------|-------|---------|
| `face-detection/face-reco.py` | Face detection with YOLOv8-face | ~45 | cv2, ultralytics, time |
| `object-detection/object_detect.py` | Object detection with YOLOv8 | ~60 | cv2, ultralytics, time |
| `pose-estimation/pose-estimation.py` | Pose estimation + action classification | ~120 | cv2, ultralytics, numpy |
| `object-counting/object_counter.py` | Object counting with SORT | ~80 | cv2, ultralytics, sort |
| `object-counting/sort.py` | SORT tracker (Kalman filter) | ~200 | numpy, scipy, filterpy |
| `emotion-detection/emotion_detect.py` | Emotion detection (YOLO + FER) | ~50 | cv2, ultralytics, fer |
| `face-recognition/simple_face_recognition.py` | Face detection with InsightFace | ~40 | cv2, insightface, numpy |

### Configuration Files

| File | Purpose |
|------|---------|
| `opencode.jsonc` | OpenCode project config (model, commands, LSP) |
| `requirements.txt` | Python dependencies |
| `.gitignore` | Git exclusion rules |
| `.github/workflows/ci.yml` | CI pipeline (lint + syntax validation) |
| `.github/workflows/validate.yml` | Weekly validation (all scripts) |
| `.github/CODEOWNERS` | Code ownership (@coderooz) |
| `.github/PULL_REQUEST_TEMPLATE.md` | PR template |
| `.github/ISSUE_TEMPLATE/bug_report.md` | Bug report template |
| `.github/ISSUE_TEMPLATE/feature_request.md` | Feature request template |

### Documentation Files

| File | Purpose |
|------|---------|
| `README.md` | Main project documentation |
| `AGENTS.md` | Root agent instructions |
| `PROJECT_STATUS.md` | Development progress tracker |
| `CONTRIBUTING.md` | Contribution guidelines |
| `LICENSE` | MIT License |
| `face-detection/README.md` | Face detection sub-project docs |
| `face-detection/AGENTS.md` | Face detection agent instructions |
| `object-detection/README.md` | Object detection sub-project docs |
| `object-detection/AGENTS.md` | Object detection agent instructions |
| `pose-estimation/README.md` | Pose estimation sub-project docs |
| `pose-estimation/AGENTS.md` | Pose estimation agent instructions |
| `object-counting/README.md` | Object counting sub-project docs |
| `object-counting/AGENTS.md` | Object counting agent instructions |
| `emotion-detection/README.md` | Emotion detection sub-project docs |
| `emotion-detection/AGENTS.md` | Emotion detection agent instructions |
| `face-recognition/README.md` | Face recognition sub-project docs |
| `face-recognition/AGENTS.md` | Face recognition agent instructions |

---

## 7. Scripts & Commands

### Development Commands

| Command | Purpose |
|---------|---------|
| `ruff check .` | Lint all Python files |
| `python -m py_compile <file>` | Validate Python syntax |
| `cd <subproject> && python <script>.py` | Run sub-project |

### OpenCode Commands (opencode.jsonc)

| Command | Template |
|---------|----------|
| `check` | Full syntax validation of all implemented scripts |
| `lint` | Ruff lint on all sub-project directories |
| `test` | Run face detection test |
| `validate` | Full validation (ruff + py_compile) |
| `validate-docs` | Cross-reference against offline docs |

---

## 8. Documentation

### README Hierarchy

```
README.md (root)
├── face-detection/README.md
├── object-detection/README.md
├── pose-estimation/README.md
├── object-counting/README.md
├── emotion-detection/README.md
├── face-recognition/README.md
├── crowd-counting/README.md (placeholder)
├── fall-detection/README.md (placeholder)
├── gesture-recognition/README.md (placeholder)
├── license-plate-detection/README.md (placeholder)
├── ppe-detection/README.md (placeholder)
└── vehicle-classification/README.md (placeholder)
```

### Agent Instructions Hierarchy

```
AGENTS.md (root)
├── face-detection/AGENTS.md
├── object-detection/AGENTS.md
├── pose-estimation/AGENTS.md
├── object-counting/AGENTS.md
├── emotion-detection/AGENTS.md
├── face-recognition/AGENTS.md
├── crowd-counting/AGENTS.md (planned)
├── fall-detection/AGENTS.md (planned)
├── gesture-recognition/AGENTS.md (planned)
├── license-plate-detection/AGENTS.md (planned)
├── ppe-detection/AGENTS.md (planned)
└── vehicle-classification/AGENTS.md (planned)
```

---

## 9. Configuration

### opencode.jsonc

- **Model:** deepseek-v4-flash-free
- **Instructions:** AGENTS.md
- **References:** https://docs.python.org/3/ (online documentation)
- **Formatter:** ruff (.py)
- **LSP:** pyright

### requirements.txt

```
ultralytics>=8.0.0
opencv-python>=4.8.0
numpy>=1.24.0
fer>=22.5.0
filterpy>=1.4.5
scipy>=1.10.0
insightface>=0.7.3
```

### .gitignore Highlights

- `models/` — All model files (.pt, .onnx, .h5, etc.)
- `venv/`, `.venv/` — Virtual environments
- `.vscode/` — IDE config
- `test/` — Project ideas reference
- `.workspace/` — Development artifacts
- `*.py[cod]` — Python bytecode

---

## 10. Architectural Relationships

### Sub-Project Pattern

Each implemented sub-project follows the same architecture:

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

### Model Dependencies

| Sub-Project | Primary Model | Secondary Model |
|-------------|--------------|-----------------|
| face-detection | yolov8n-face.pt | — |
| object-detection | yolov8n.pt | — |
| pose-estimation | yolov8n-pose.pt | — |
| object-counting | yolov8n.pt | — |
| emotion-detection | yolov8n-face.pt | FER CNN (auto-download) |
| face-recognition | — | InsightFace buffalo_l (auto-download) |

### Shared Resources

- All sub-projects use `../models/` for model files (relative paths)
- All sub-projects use OpenCV for webcam capture and display
- All sub-projects exit on ESC key press
- `object-counting/sort.py` is used by `object-counting/object_counter.py`

---

## 11. Known Constraints

| Constraint | Impact |
|------------|--------|
| Windows-style paths | Model paths use backslashes in some places |
| Webcam required | All sub-projects need a webcam for inference |
| Model files not tracked | Must be downloaded separately (see READMEs) |
| No GPU acceleration | CPU inference by default |
| Single-threaded | No async/parallel processing |
| SORT tracker state | `KalmanBoxTracker.count` never resets |

---

## 12. Maintenance Log

| Date | Version | Change | Verified By |
|------|---------|--------|-------------|
| 2026-09-06 | 1.0 | Initial PRI creation | OpenCode agent |
| 2026-09-06 | 1.1 | Phases 1-6: governance, docs, deps, code quality fixes | OpenCode agent |
| 2026-09-09 | 1.2 | Preservation: portable paths, CHANGELOG, Developer Notes | OpenCode agent |

---

## 13. Verification Checklist

- [x] All directories verified via filesystem inspection
- [x] All Python scripts verified for existence and content
- [x] All configuration files verified
- [x] All documentation files verified
- [x] Model requirements verified per sub-project
- [x] Git remote verified (coderooz/YOLO-PROJECT-PYTHON)
- [x] CI workflows verified
- [x] Dependencies verified against actual imports
- [x] Code quality fixes applied (FPS, zero-division, imports)
- [x] .workspace/ governance structure created
- [x] MCP memory synchronized

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Changed
- Portable documentation references (removed Windows-specific paths from all AGENTS.md files)
- Updated opencode.jsonc to use online Python docs instead of local offline docs
- Fixed CONTRIBUTING.md model path typo (`.py` to `.pt`)

### Added
- CHANGELOG.md (this file)
- DEVELOPMENT.md (developer notes)
- GitHub configuration: CI workflows, issue templates, PR template, CODEOWNERS
- Sub-project AGENTS.md files for all 12 sub-projects
- Sub-project README files for planned sub-projects
- Sub-project LICENSE files for implemented sub-projects
- Sub-project requirements.txt for face-recognition, object-detection, object-counting
- Sub-project .gitignore files for implemented sub-projects
- Sub-project opencode.jsonc for implemented sub-projects

---

## [0.2.0] - 2026-09-06

### Added
- PRI (Project Reference Index) at `.opencode/reference/PROJECT_REFERENCE_INDEX.md`
- `.workspace/` directory structure
- MCP project descriptor and project map
- AGENTS.md for 6 planned sub-projects
- README placeholders for 6 planned sub-projects

### Fixed
- AGENTS.md model path typo (`.py` to `.pt`)
- README backtick issues (4 backticks to 3)
- Removed invalid LICENSE badge links from sub-project READMEs
- Added `filterpy`, `scipy`, `insightface` to requirements.txt

---

## [0.1.0] - 2026-06-14

### Added
- OpenCode configuration (`opencode.jsonc`)
- `AGENTS.md` for AI agent instructions
- Updated README with full project table and badges
- `LICENSE` (MIT)
- `CONTRIBUTING.md`
- `requirements.txt` with pinned dependencies
- `PROJECT_STATUS.md`

---

## [0.0.1] - 2025-11-17

### Added
- Initial commit
- Face detection (`face-detection/face-reco.py`)
- Object detection (`object-detection/object_detect.py`)
- Pose estimation (`pose-estimation/pose-estimation.py`)
- Object counting with SORT tracker (`object-counting/`)
- Emotion detection (`emotion-detection/emotion_detect.py`)
- Face recognition stub (`face-recognition/simple_face_recognition.py`)
- `.gitignore`
- `README.md`

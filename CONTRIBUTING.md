# Contributing to YOLO Projects

Thank you for your interest in contributing! This guide will help you get started.

## Getting Started

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/YOLO-PROJECT-PYTHON.git
   cd YOLO-PROJECT-PYTHON
   ```
3. **Create** a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
4. **Install** dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Adding a New Sub-Project

1. Create a new directory: `your-project-name/`
2. Add your Python script(s)
3. Add a `README.md` with:
   - Description
   - Model requirements
   - Usage instructions
   - Preview screenshot (optional)
4. Update the main `README.md` to include your project
5. Update `AGENTS.md` sub-projects table

## Code Style

- **Python 3.10+** with type hints
- **OpenCV** for webcam/display operations
- **YOLOv8** via `ultralytics` for inference
- Keep scripts self-contained and well-documented
- Use relative model paths: `../models/<model>.pt`
- ESC key to exit, `q` as alternative

## Model Files

- **Never commit** model files (`*.pt`, `*.onnx`, `*.pth`)
- Document model download links in your sub-project README
- Place models in `./models/` directory

## Pull Requests

1. Keep PRs focused on one sub-project or improvement
2. Include a clear description of what changed
3. Test with your webcam before submitting
4. Add/update README documentation

## Issues

- Use GitHub Issues for bug reports and feature requests
- Include: OS, Python version, camera model, error output

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

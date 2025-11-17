# 🧠 YOLO Projects (Python)

This repository contains a collection of small, practical projects built using **YOLOv8** for real-time computer vision tasks.  
Each sub-project demonstrates a different use-case of YOLO, such as **face detection** or **general object detection** using a webcam feed.

---

## 📌 Projects Included

### 🔹 1. Face Detection  
Real-time detection of human faces using a YOLOv8-face model.  
📁 Folder: `./face-detection/`  
🖼 Preview:  
![Face Detection](./image/face-detection.png)

---

### 🔹 2. Object Detection  
Real-time detection of general objects using YOLOv8 models.  
📁 Folder: `./object-detection/`  
🖼 Preview:  
![Object Detection](./image/object_detection.png)

---

## ⚙️ Requirements

Install dependencies:

```bash
pip install -r requirements.txt
````

Required major packages:

* `ultralytics`
* `opencv-python`
* `numpy`

---

## 📦 Models (Not Included in Repo)

Place downloaded models inside:

```
./models/
```

### 🔽 Recommended Model Downloads

| Model             | Description                             | Download                                                                                                                                                                                                           |
| ----------------- | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `yolov8n.pt`      | General object detection (nano version) | Ultralytics: [https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt](https://github.com/ultralytics/assets/releases/download/v8.1.0/yolov8n.pt)                                                |
| `yolov8s.pt`      | More accurate + heavier                 | HF: [https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8s.pt?download=true](https://huggingface.co/Ultralytics/YOLOv8/resolve/main/yolov8s.pt?download=true)                                             |
| `yolov8n-face.pt` | Specialized face detection              | Google Drive: [https://drive.usercontent.google.com/u/0/uc?id=1qcr9DbgsX3ryrz2uU8w4Xm3cOrRywXqb&export=download](https://drive.usercontent.google.com/u/0/uc?id=1qcr9DbgsX3ryrz2uU8w4Xm3cOrRywXqb&export=download) |
| (Alt face model)  | Extra mirror link                       | [https://drive.usercontent.google.com/u/0/uc?id=1vFMGW8xtRVo9bfC9yJVWWGY7vVxbLh94&export=download](https://drive.usercontent.google.com/u/0/uc?id=1vFMGW8xtRVo9bfC9yJVWWGY7vVxbLh94&export=download)               |

---

## 🚀 Running the Projects

### Face Detection

```bash
cd face-detection
python face-reco.py
```

### Object Detection

```bash
cd object-detection
python object_detect.py
```

Make sure your webcam is connected.

---

## 📝 Repository Structure

```
YOLO/
│── face-detection/
│   ├── face-reco.py
│   └── README.md
│
│── object-detection/
│   ├── object_detect.py
│   └── README.md
│
│── image/
│   ├── face-detection.png
│   └── object_detection.png
│
│── models/       # (Not tracked by Git)
│── requirements.txt
│── .gitignore
│── README.md
```

---

## ⚠️ Note About `.gitignore` and Large Files

Model files (`*.pt`, `*.onnx`, etc.) and the `models/` folder are intentionally ignored to keep the repository lightweight.

---

## 📚 Tech Used

* Python
* OpenCV
* Ultralytics YOLOv8
* Real-time webcam inference

---

## 🤝 Contributions

Open to ideas, improvements, and new YOLO sub-projects!


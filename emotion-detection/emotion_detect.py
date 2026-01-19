import cv2
from ultralytics import YOLO
from fer.fer import FER
import numpy as np

# 1. Load YOLO face detector
face_model = YOLO("../models/yolov8n-face.pt")

# 2. Load emotion detector (FER — pre-trained CNN)
emotion_detector = FER(mtcnn=True)

# 3. Start webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = face_model(frame)[0]
    annotated = frame.copy()

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])

        face = frame[y1:y2, x1:x2]
        if face.size == 0:
            continue

        # 4. Emotion detection using FER
        emotions = emotion_detector.detect_emotions(face)

        if emotions:
            top_emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)
        else:
            top_emotion = "Unknown"

        # Draw box
        cv2.rectangle(annotated, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Label
        cv2.putText(
            annotated,
            top_emotion,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (255, 255, 255),
            2,
        )

    cv2.imshow("Emotion Detection", annotated)

    # ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO
import time

# Load the YOLO face model
model = YOLO("../models/yolov8n-face.pt")  # path to model

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access your webcam.")
    exit()

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run face detection
    results = model(frame, conf=0.5)[0]

    # Plot detections on frame
    annotated_frame = results.plot()

    # FPS calculation (time-based)
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if prev_time != 0 else 0
    prev_time = curr_time

    cv2.putText(
        annotated_frame,
        f"FPS: {fps}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("YOLO Face Detection", annotated_frame)

    # Press ESC to quit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

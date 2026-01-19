import cv2
import numpy as np
from ultralytics import YOLO
from sort import Sort

model = YOLO("../models/yolov8n.pt")
tracker = Sort()

cap = cv2.VideoCapture(0)

# Horizontal counting line
LINE_Y = 350
total_count = 0
counted_ids = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]
    detections = []

    # Convert YOLO boxes → SORT format
    for box in results.boxes:
        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
        conf = float(box.conf[0])
        cls = int(box.cls[0])  # class id

        # Count PEOPLE only (cls=0). Change as needed.
        if conf > 0.5 and cls == 0:
            detections.append([x1, y1, x2, y2, conf])

    detections = np.array(detections)

    # Update tracker
    tracked_objects = tracker.update(detections)

    # Draw counting line
    cv2.line(frame, (0, LINE_Y), (frame.shape[1], LINE_Y), (0, 255, 255), 2)

    # Process tracked objects
    for obj_id, bbox in tracked_objects:
        x1, y1, x2, y2 = map(int, bbox)
        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        # Draw bounding box + ID
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 200, 0), 2)
        cv2.putText(frame, f"ID {obj_id}", (x1, y1 - 7),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

        # Check if object crosses the counting line
        if cy > LINE_Y and obj_id not in counted_ids:
            counted_ids.add(int(obj_id))
            total_count += 1

    # Display count
    cv2.putText(frame, f"Count: {total_count}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Object Counter", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()

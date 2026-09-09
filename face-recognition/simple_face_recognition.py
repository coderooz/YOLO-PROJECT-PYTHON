import cv2
from insightface.app import FaceAnalysis
import time

# Load face recognition model
app = FaceAnalysis(name="buffalo_l", providers=["CPUExecutionProvider"])
app.prepare(ctx_id=0, det_size=(640, 640))

# Load webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access webcam")
    exit()

prev_time = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    faces = app.get(frame)
    annotated = frame.copy()

    for face in faces:
        box = face.bbox.astype(int)
        name = "Unknown"

        # Draw bounding box
        cv2.rectangle(annotated, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

        # Put label
        cv2.putText(annotated, name, (box[0], box[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 2)

    # FPS calculation (time-based)
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time)) if prev_time != 0 else 0
    prev_time = curr_time

    cv2.putText(
        annotated,
        f"FPS: {fps}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Face Recognition", annotated)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

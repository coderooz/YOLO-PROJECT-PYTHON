import cv2
from ultralytics import YOLO
import numpy as np

model = YOLO("../models/yolov8n-pose.pt")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not access your webcam.")
    exit()


def classify_action(keypoints):
    """
    keypoints: numpy array of shape (17, 3) → (x, y, conf)
    """

    # Safely extract (x, y, conf)
    def safe_get(idx):
        if keypoints[idx][2] > 0.5:   # confidence threshold
            return keypoints[idx]
        return None

    nose = safe_get(0)
    left_wrist = safe_get(9)      # YOLOv8-pose keypoint index
    right_wrist = safe_get(10)
    left_shoulder = safe_get(5)
    right_shoulder = safe_get(6)

    action = "Unknown"

    # 👋 Hi — one wrist above nose
    if nose is not None:
        if (left_wrist is not None and left_wrist[1] < nose[1]) or \
           (right_wrist is not None and right_wrist[1] < nose[1]):
            action = "Hi 👋"

    # 🙌 Hands Up — both wrists above both shoulders
    if left_wrist is not None and right_wrist is not None and \
       left_shoulder is not None and right_shoulder is not None:
        if left_wrist[1] < left_shoulder[1] and right_wrist[1] < right_shoulder[1]:
            action = "Hands Up 🙌"

    return action


while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.5)[0]
    annotated_frame = results.plot()

    action_text = "No Person"

    if results.keypoints is not None and len(results.keypoints) > 0:
        try:
            # Extract XY (17x2)
            xy = results.keypoints[0].xy[0].cpu().numpy()

            # Extract CONF (17,)
            conf = results.keypoints[0].conf[0].cpu().numpy()

            # Merge into (17, 3) array → (x, y, conf)
            keypoints = np.hstack([xy, conf.reshape(-1, 1)])

            # Classify action
            action_text = classify_action(keypoints)

        except Exception as e:
            print("Keypoint parsing error:", e)
            action_text = "Error"

    # Display action text
    cv2.putText(
        annotated_frame,
        f"Action: {action_text}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2
    )

    cv2.imshow("YOLO Pose Action Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

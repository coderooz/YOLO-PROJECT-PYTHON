# SORT tracker implementation (clean + fixed for YOLO)
# Source adapted from original https://github.com/abewley/sort

import numpy as np
from filterpy.kalman import KalmanFilter
from scipy.optimize import linear_sum_assignment


def iou(bb_test, bb_gt):
    xx1 = np.maximum(bb_test[0], bb_gt[0])
    yy1 = np.maximum(bb_test[1], bb_gt[1])
    xx2 = np.minimum(bb_test[2], bb_gt[2])
    yy2 = np.minimum(bb_test[3], bb_gt[3])
    w = np.maximum(0., xx2 - xx1)
    h = np.maximum(0., yy2 - yy1)
    wh = w * h
    area_test = (bb_test[2] - bb_test[0]) * (bb_test[3] - bb_test[1])
    area_gt = (bb_gt[2] - bb_gt[0]) * (bb_gt[3] - bb_gt[1])
    union = area_test + area_gt - wh
    if union <= 0:
        return 0.0
    return wh / union


class KalmanBoxTracker:
    """
    This tracks ONE object using a Kalman filter.
    """

    count = 0

    def __init__(self, bbox):
        # Kalman filter: x, y, s, r, and their velocities
        self.kf = KalmanFilter(dim_x=7, dim_z=4)
        self.kf.F = np.eye(7)
        self.kf.H = np.eye(4, 7)

        # FIX: reshape YOLO bbox correctly (4,1)
        bbox = np.reshape(bbox[:4], (4, 1))
        self.kf.x[:4] = bbox

        self.time_since_update = 0
        self.id = KalmanBoxTracker.count
        KalmanBoxTracker.count += 1

    def update(self, bbox):
        bbox = np.reshape(bbox[:4], (4, 1))
        self.kf.update(bbox)
        self.time_since_update = 0

    def predict(self):
        self.kf.predict()
        self.time_since_update += 1
        return self.kf.x[:4]


class Sort:
    """
    SORT tracker (multiple object tracker)
    """

    def __init__(self, max_age=10, min_hits=2):
        self.max_age = max_age
        self.min_hits = min_hits
        self.trackers = []

    def update(self, detections):
        results = []

        # Predict new positions for all existing trackers
        predicted = []
        for t in self.trackers:
            predicted.append(t.predict())

        # Match detected boxes to predicted trackers
        if len(predicted) > 0 and len(detections) > 0:
            cost_matrix = np.zeros((len(predicted), len(detections)))

            for i, p in enumerate(predicted):
                for j, d in enumerate(detections):
                    cost_matrix[i, j] = 1 - iou(p.flatten(), d[:4])

            row, col = linear_sum_assignment(cost_matrix)

            matched = set()
            for r, c in zip(row, col):
                if cost_matrix[r][c] < 0.8:  # iou > 0.2
                    self.trackers[r].update(detections[c])
                    matched.add(c)

            # Add unmatched detections as new trackers
            for d_idx, det in enumerate(detections):
                if d_idx not in matched:
                    self.trackers.append(KalmanBoxTracker(det))

        else:
            # No match, create trackers for all detections
            for det in detections:
                self.trackers.append(KalmanBoxTracker(det))

        # Return all tracker states
        tracked_objects = []
        new_trackers = []

        for t in self.trackers:
            pos = t.kf.x[:4].flatten()
            tracked_objects.append((t.id, pos))

            # Keep tracker if not too old
            if t.time_since_update < self.max_age:
                new_trackers.append(t)

        self.trackers = new_trackers
        return tracked_objects

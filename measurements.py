import cv2
import numpy as np
import mediapipe as mp
from mediapipe.python.solutions import pose as mp_pose

# MediaPipe Pose Initialization
pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

def calculate_inches(pixel_dist, calibration_ratio):
    return pixel_dist * calibration_ratio

def get_body_measurements(frame, calibration_ratio):
    results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    if results.pose_landmarks:
        landmarks = results.pose_landmarks.landmark
        h, w, _ = frame.shape
        
        # Chest: Landmarks 11 (Left Shoulder) & 12 (Right Shoulder)
        sh_l = np.array([landmarks[11].x * w, landmarks[11].y * h])
        sh_r = np.array([landmarks[12].x * w, landmarks[12].y * h])
        pixel_chest = np.linalg.norm(sh_l - sh_r)
        
        # Waist: Landmarks 23 (Left Hip) & 24 (Right Hip)
        hip_l = np.array([landmarks[23].x * w, landmarks[23].y * h])
        hip_r = np.array([landmarks[24].x * w, landmarks[24].y * h])
        pixel_waist = np.linalg.norm(hip_l - hip_r)

        actual_chest = calculate_inches(pixel_chest, calibration_ratio) * 2.2
        actual_waist = calculate_inches(pixel_waist, calibration_ratio) * 2.2
        return round(actual_chest, 1), round(actual_waist, 1), results.pose_landmarks
    return None, None, None

def get_skin_color(frame, landmarks_obj):
    if not landmarks_obj:
        return "Unknown", []
        
    landmarks = landmarks_obj.landmark
    h, w, _ = frame.shape
    
    # IndexError Fix: np.clip ensures cx/cy stay inside frame boundaries
    cx = int(np.clip(landmarks[1].x * w, 0, w - 1))
    cy = int(np.clip(landmarks[1].y * h, 0, h - 1))
    
    color_bgr = frame[cy, cx]
    brightness = np.mean(color_bgr)
    
    if brightness > 180:
        return "Fair", ["Navy Blue", "Maroon", "Dark Green"]
    elif brightness > 120:
        return "Medium/Wheatish", ["Mustard", "Olive Green", "Sky Blue"]
    else:
        return "Dark/Deep", ["White", "Pastel Pink", "Light Grey"]
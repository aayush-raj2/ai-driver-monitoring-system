import cv2
import mediapipe as mp
import numpy as np
from scipy.spatial import distance
from yawn import mouth_aspect_ratio
from head_pose import get_head_tilt
from logger import log_event
import config

BaseOptions = mp.tasks.BaseOptions
VisionRunningMode = mp.tasks.vision.RunningMode
FaceLandmarker = mp.tasks.vision.FaceLandmarker
FaceLandmarkerOptions = mp.tasks.vision.FaceLandmarkerOptions

options = FaceLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="models/face_landmarker.task"),
    running_mode=VisionRunningMode.VIDEO,
)

landmarker = FaceLandmarker.create_from_options(options)

LEFT_EYE = [33, 160, 158, 133, 153, 144]
RIGHT_EYE = [362, 385, 387, 263, 373, 380]
MOUTH = [13,14,15,16,17,18,19,20]

eye_counter = 0
yawn_counter = 0

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2.0 * C)

def detect(frame, timestamp):
    global eye_counter, yawn_counter

    h, w = frame.shape[:2]
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb)
    result = landmarker.detect_for_video(mp_image, timestamp)

    if result.face_landmarks:
        for face in result.face_landmarks:

            left_eye = np.array([(int(face[i].x*w), int(face[i].y*h)) for i in LEFT_EYE])
            right_eye = np.array([(int(face[i].x*w), int(face[i].y*h)) for i in RIGHT_EYE])

            ear = (eye_aspect_ratio(left_eye) + eye_aspect_ratio(right_eye)) / 2

            mouth = np.array([(int(face[i].x*w), int(face[i].y*h)) for i in MOUTH])
            mar = mouth_aspect_ratio(mouth)

            head_tilt = get_head_tilt(face)

            if ear < config.EAR_THRESHOLD:
                eye_counter += 1
                if eye_counter > config.EYE_AR_CONSEC_FRAMES:
                    cv2.putText(frame, "DROWSY", (50,100),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)
                    log_event("Drowsiness")
            else:
                eye_counter = 0

            if mar > config.MAR_THRESHOLD:
                yawn_counter += 1
                if yawn_counter > config.YAWN_FRAMES:
                    cv2.putText(frame, "YAWNING", (50,150),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 3)
                    log_event("Yawn")
            else:
                yawn_counter = 0

            if abs(head_tilt) > config.HEAD_TILT_THRESHOLD:
                cv2.putText(frame, "HEAD TILT", (50,200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 3)
                log_event("Head Tilt")

    return frame

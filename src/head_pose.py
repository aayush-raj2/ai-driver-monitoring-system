def get_head_tilt(face_landmarks):
    left = face_landmarks[33]
    right = face_landmarks[263]

    dx = right.x - left.x
    dy = right.y - left.y

    return dy / (dx + 1e-6)

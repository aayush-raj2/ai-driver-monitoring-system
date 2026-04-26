import cv2

def evaluate(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = 0
    detections = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames += 1

        # Replace with actual detection call
        detected = False

        if detected:
            detections += 1

    print("Detection Rate:", detections/frames)

evaluate("data/sample_video.mp4")

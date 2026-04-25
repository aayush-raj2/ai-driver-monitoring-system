import cv2
from detector import detect

cap = cv2.VideoCapture(0)
timestamp = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = detect(frame, timestamp)
    timestamp += 1

    cv2.imshow("Driver Monitoring", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()

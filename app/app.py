import streamlit as st
import cv2
from src.detector import detect

st.title("🚗 Driver Monitoring System")

run = st.checkbox("Start Camera")
frame_window = st.image([])

cap = cv2.VideoCapture(0)
timestamp = 0

while run:
    ret, frame = cap.read()
    if not ret:
        break

    frame = detect(frame, timestamp)
    timestamp += 1

    frame_window.image(frame, channels="BGR")

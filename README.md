# 🚗 AI Driver Monitoring System

## 📌 Overview
This project is a real-time AI-based **Driver Monitoring System** designed to detect:

- Eye closure (Drowsiness)
- Yawning (Fatigue)
- Head tilt (Inattention)

The system combines multiple behavioral signals to improve reliability over single-metric approaches.

---

## 🧠 Features

### 👁 Eye Drowsiness Detection
- Based on Eye Aspect Ratio (EAR)
- Detects prolonged eye closure

### 😮 Yawn Detection
- Uses Mouth Aspect Ratio (MAR)
- Identifies yawning patterns

### 🧭 Head Tilt Detection
- Estimates head orientation using facial landmarks
- Detects driver distraction or nodding

### 📊 Event Logging
- Records drowsiness events with timestamps
- Stores logs in CSV format

### 📈 Accuracy Evaluation
- Runs detection on pre-recorded video dataset
- Measures detection frequency and consistency

### 🌐 Streamlit UI
- Real-time visualization
- Displays alerts and metrics

---

## ⚙️ System Pipeline

1. Capture video (webcam or file)
2. Detect face landmarks (MediaPipe)
3. Compute:
   - EAR (eyes)
   - MAR (mouth)
   - Head angle
4. Apply thresholds + temporal filtering
5. Trigger alerts + log events
6. Display results via UI

---

## 📦 Requirements

```bash
opencv-python
mediapipe
numpy
streamlit
pandas
scipy
playsound
```
---

## ▶️ Run the System

- Run Detection
```bash
python src/main.py
```
- Run UI
```
streamlit run app/app.py
```
- Run Evaluation
```
python evaluation/evaluate.py
```
---

## 📊 Output
- Real-time alerts on screen
- Event logs stored in /logs/events.csv
- Evaluation metrics printed in console
---
## ⚠ Limitations
- Sensitive to lighting
- Requires frontal face
- No deep learning model (rule-based)
---
## 🚀 Future Improvements
- CNN-based fatigue detection
- Mobile deployment
- Multi-person tracking
- Night vision support
 ---

## 👨‍💻 Author

Aayush Raj  
B.Tech CSE – Software Engineering   

# 🏋️ AI Gym Trainer

An AI-powered gym training assistant that uses computer vision and pose estimation to count your exercise repetitions in real time. Currently tracks **bicep curls** — with the angle of the right arm detected frame-by-frame, the system counts every complete rep and displays a live progress bar.

---

## ✨ Features

- **Real-time pose detection** powered by [MediaPipe](https://mediapipe.dev/)
- **Automatic rep counting** — no buttons, no timers, just move
- **Live progress bar** showing how far through the current rep you are (0 → 100%)
- **Rep counter panel** displayed on screen
- Works with a **webcam feed** or a **pre-recorded video file**

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Core language |
| OpenCV (`cv2`) | Video capture, drawing overlays |
| MediaPipe | Human pose landmark detection |
| NumPy | Angle-to-percentage interpolation |

---

## 📋 Prerequisites

- Python 3.8 or higher
- A webcam **or** a compatible `.mp4` video file

---

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Mpradeep-dev/AI_Trainer.git
   cd AI_Trainer
   ```

2. **Install dependencies**
   ```bash
   pip install opencv-python mediapipe numpy
   ```

---

## ▶️ Usage

### Run with the sample video (default)
```bash
python main.py
```
By default `main.py` reads `res/gym1.mp4`.

### Switch to webcam input
Open `main.py` and change line 5:
```python
# Use webcam
vid = cv.VideoCapture(0)

# Use a video file
vid = cv.VideoCapture("res/gym1.mp4")
```

### Controls
| Key | Action |
|-----|--------|
| `Esc` | Quit |

---

## 📁 Project Structure

```
AI_Trainer/
├── main.py          # Entry point — video loop, rep counting, UI overlays
├── pose_module.py   # Reusable pose detector class (MediaPipe wrapper)
├── res/
│   └── gym1.mp4     # Sample workout video
└── README.md
```

---

## 🧠 How It Works

1. **Frame capture** — each video frame is read and resized to 2× for better visibility.
2. **Pose landmarks** — MediaPipe identifies 33 body key-points per frame.
3. **Angle calculation** — the angle at the elbow (shoulder → elbow → wrist, landmarks 12-14-16) is computed using `atan2`.
4. **Rep counting** — the angle is interpolated to a 0–100% range. A full rep is counted when the arm goes from 0 % → 100 % → 0 % (or vice-versa).
5. **Overlays drawn**:
   - Right-side magenta bar = current rep progress.
   - Bottom-left green panel = total reps completed.

### Pose Landmarks Used

```
12 → Right Shoulder
14 → Right Elbow  (vertex of the angle)
16 → Right Wrist
```

---

## 🔧 `pose_module.py` — Detector API

```python
dec = pm.detector()

img  = dec.find_pose(img, draw=True)   # Draw skeleton on frame
lmks = dec.get_conn(img, draw=False)   # Returns list of [id, cx, cy]
angle = dec.find_angle(p1, p2, p3, img, draw=True)  # Angle at p2
```

---

## 🗺️ Roadmap / Future Improvements

- [ ] Support multiple exercises (squats, push-ups, shoulder press)
- [ ] Voice feedback announcements ("Rep 5 done!")
- [ ] Web or desktop GUI with session history
- [ ] Webcam auto-detection with file-path fallback
- [ ] Export rep data to CSV / JSON

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

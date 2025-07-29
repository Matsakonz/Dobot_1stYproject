# 🎯 Dobot Arm Color Sorting Robot

This project demonstrates an automated **color sorting robot** using a **Dobot robotic arm** and **OpenCV (cv2)**. The system detects objects of different colors (e.g., red, blue, yellow) using a camera, counts them, and commands the Dobot to move and sort the objects into separate areas based on their color.

---

## 📸 Features

- Detect and count objects of specific colors (e.g., red, blue, yellow)
- Control Dobot arm movement with Python
- Automatically pick and place objects in separate zones based on detected color
- Live camera feed and real-time processing using OpenCV

---

## 🧰 Technologies Used

- Python 3
- OpenCV (`cv2`)
- Dobot Python SDK (or custom communication interface)
- Serial communication (`pyserial`, if applicable)

---

## 🛠️ How It Works

1. The camera captures a live video feed.
2. The software uses OpenCV to detect and count colored objects.
3. For each object detected:
   - The color is identified (red, blue, yellow).
   - The position is used to command the Dobot arm.
4. The Dobot picks up the object and places it into a designated zone based on its color.

---

### 🧾 Example Output:
```bash
Detected colors:
Red: 2
Blue: 1
Yellow: 3
```

---

## 📂 Project Structure
```bash
dobot-color-sorting/
├── main.py             # Main control script
├── camera.py           # Handles video capture and color detection
├── dobot_control.py    # Sends commands to the Dobot arm
├── utils.py            # Utility functions for color masking, etc.
├── README.md           # Project description
```

---

## 🎮 Controls

- Press `s` to save current object positions (optional)
- Press `e` to stop the program

---

## ⚙️ Installation & Setup
1. Clone this repository:
```bash
git clone https://github.com/yourusername/dobot-color-sorting.git
cd dobot-color-sorting
```
2. Install dependencies:
```bash
pip install opencv-python pyserial
```
3. Connect your Dobot arm via USB and ensure it's powered on.
4. Run the main script:
```bash
python main.py
```

---

## 🎨 Supported Colors
You can modify the HSV range in camera.py to adjust or add more colors:
- 🔴 Red
- 🔵 Blue
- 🟡 Yellow

---

## 📌 Notes
- Ensure the lighting conditions are consistent for better color detection accuracy.
- The sorting zones and pickup coordinates should be calibrated according to your setup.

---

## 🧠 Future Improvements
- Add GUI for manual control and color calibration
- Use a pretrained ML model for more accurate object classification
- Integrate with a conveyor belt for full automation

---

## 🧑‍💻 Author
Matsakon T.
Robotics Engineering Student | Automation Enthusiast
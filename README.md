# 🤖 Dobot Arm Color Sorting Robot

This project demonstrates an automated **color sorting robot** using a **Dobot robotic arm** and **OpenCV (cv2)**. The system detects objects of different colors (e.g., red, blue, yellow) using a camera, counts them, and commands the Dobot to move and sort the objects into separate areas based on their color.

---

## 📸 Features

- Detect and count objects of specific colors (e.g., red, blue, yellow)
- Control Dobot arm movement with Python
- Automatically pick and place objects in separate zones based on detected color
- Live camera feed and real-time processing using OpenCV

## 🧰 Technologies Used

- Python 3
- OpenCV (`cv2`)
- Dobot Python SDK (or custom communication interface)

## 🛠️ How It Works

1. The camera captures a live video feed.
2. The software uses OpenCV to detect and count colored objects.
3. For each object detected:
   - The color is identified (red, blue, yellow).
   - The position is used to command the Dobot arm.
4. The Dobot picks up the object and places it into a designated zone based on its color.

### 🧾 Example Output:
```bash
Detected colors:
Blue 1: (507, 264)
Blue 2: (142, 209)
Blue 3: (115, 148)
Yellow 1: (557, 240)
Red 1: (406, 309)
Red 2: (92, 100)
Green 1: (455, 287)
```

## 📂 Project Structure
```bash
Dobot_1stYproject/
├── main.py             # Main control script
├── calibration.py      # Set a start and stop position   
├── mode1.py            # Sends commands to the Dobot arm
├── mode2.py            # Handles video capture and color detection 
├── README.md           # Project description
```

## 🎮 Controls

- Press `s` to save current object positions (optional)
- Press `e` to stop the program

## ⚙️ Installation & Setup
1. Clone this repository:
```bash
git clone https://github.com/Matsakonz/Dobot_1stYproject.git
cd Dobot_1stYproject
```
2. Install dependencies:
```bash
pip install opencv-python
pip install pydobot2
```
3. Connect your Dobot arm via USB and ensure it's powered on.
4. Run the main script:
```bash
python main.py
```

## 🎨 Supported Colors
You can modify the HSV range in mode2.py to adjust or add more colors:
- 🔴 Red
- 🔵 Blue
- 🟡 Yellow
- 🟢 Green

## 📌 Notes
- Ensure the lighting conditions are consistent for better color detection accuracy.
- The sorting zones and pickup coordinates should be calibrated according to your setup.

## 🧠 Future Improvements
- Add GUI for manual control and color calibration
- Use a pretrained ML model for more accurate object classification
- Integrate with a conveyor belt for full automation

## 🧑‍💻 Author
**Matsakon T.**
Robotics Engineering Student | Automation Enthusiast

## 📄 License
This project is licensed under the [WTFPL](http://www.wtfpl.net/about/) – Do What the F*ck You Want to Public License.

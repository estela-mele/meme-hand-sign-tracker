# 🎬 Meme Hand Sign Tracker

![Python](https://img.shields.io/badge/Python-3.10-blue) ![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0-green) ![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10.21-orange) ![NumPy](https://img.shields.io/badge/NumPy-1.26.4-yellow)

A project to track hand signs for memes using **MediaPipe**, **OpenCV**, and **NumPy**.


## 📦 1. Setup

Clone the repository:

`git clone https://github.com/estela-mele/meme-hand-sign-tracker.git`

`cd meme-hand-sign-tracker`

## 🛠 2. Create and Activate Virtual Environment

macOS / Linux

`python3 -m venv mp_env`

`source mp_env/bin/activate`

Windows

`python -m venv mp_env`

`mp_env\Scripts\activate`

💡 Make sure your terminal is using the project’s virtual environment.

## 📥 3. Install dependencies:

`pip install --upgrade pip setuptools wheel`

`pip install -r requirements.txt`


## ▶️ 4. Running the Project
   
Terminal:

`python meme-tracker.py`


## 🖥 5. VS Code:

Press Cmd+Shift+P (or Ctrl+Shift+P on Windows)

Select Python: Select Interpreter

Choose your environment: ~/meme-hand-sign-tracker/mp_env/bin/python


## ✅ 6. Verify Installation
Run the following command to make sure all libraries are correctly installed:

`python -c "import mediapipe as mp; import cv2; import numpy; print('MediaPipe:', mp.__version__, 'OpenCV:', cv2.__version__, 'Numpy:', numpy.__version__)"`


Expected output:

MediaPipe: 0.10.21 OpenCV: 4.11.0 Numpy: 1.26.4


## 📌 Notes:

Each time you want to run the project:

`source mp_env/bin/activate`

`python meme-tracker.py`

<details> <summary>💡 OPTIONAL TIPS </summary>

Make sure your camera is working properly for hand tracking.

Avoid committing mp_env/ to GitHub; it is included in .gitignore.

If you run into errors, try updating your packages:

`pip install --upgrade pip setuptools wheel`
`pip install --upgrade -r requirements.txt`

</details>

❤️ Contributions

Contributions, issues, and feature requests are welcome!

Meme Hand Sign Tracker

1. Setup
Clone the repository:
git clone https://github.com/estela-mele/meme-hand-sign-tracker.git
cd meme-hand-sign-tracker

2. Create and activate the virtual environment:
python3 -m venv mp_env
source mp_env/bin/activate      # macOS / Linux
# mp_env\Scripts\activate       # Windows

3. Install dependencies:
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

4. Running the Project
Terminal:
python meme-tracker.py

5. VS Code:
Press Cmd+Shift+P (or Ctrl+Shift+P on Windows)
Select Python: Select Interpreter
Choose: ~/meme-hand-sign-tracker/mp_env/bin/python

6. Verify Installation
Run the following command to make sure all libraries are correctly installed:
python -c "import mediapipe as mp; import cv2; import numpy; print('MediaPipe:', mp.__version__, 'OpenCV:', cv2.__version__, 'Numpy:', numpy.__version__)"

Expected output:
MediaPipe: 0.10.21 OpenCV: 4.11.0 Numpy: 1.26.4

Notes:
Then just run this everytime:
source mp_env/bin/activate
python meme-tracker.py


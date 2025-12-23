TERMINAL:
cd ~/meme-hand-sign-tracker
source mp_env/bin/activate
python meme-tracker.py

VS Code interpreter: (cmd+shift+p: python:select interpreter)
~/meme-hand-sign-tracker/mp_env/bin/python

VERIFY:
python -c "import mediapipe as mp; import cv2; import numpy; print('MediaPipe:', mp.__version__, 'OpenCV:', cv2.__version__, 'Numpy:', numpy.__version__)"
MediaPipe: 0.10.21 OpenCV: 4.11.0 Numpy: 1.26.4

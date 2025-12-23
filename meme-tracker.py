import cv2
import mediapipe as mp

# Initialize MediaPipe solutions
mp_hands = mp.solutions.hands
mp_face = mp.solutions.face_mesh
mp_draw = mp.solutions.drawing_utils

# Load images
images = {
    "base": cv2.imread("memes/peace.jpg"),
    "a": cv2.imread("memes/scream.jpg"),
    "b": cv2.imread("memes/rise-eyebrows.jpg"),
    "c": cv2.imread("memes/pause.jpg"),
    "e": cv2.imread("memes/actually.jpg"),
    "f": cv2.imread("memes/fist.jpg"),
    "g": cv2.imread("memes/loser.jpg"),
}

# Check if images are loaded
if any(img is None for img in images.values()):
    print("Error: Some images not found!")
    exit()

current_img = images["base"].copy()

# Initialize MediaPipe hands and face
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5)
face_mesh = mp_face.FaceMesh(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)

def fingers_up(hand_landmarks):
    lm = hand_landmarks.landmark
    tips = [4, 8, 12, 16, 20]
    pip = [3, 6, 10, 14, 18]

    fingers = []
    fingers.append(lm[tips[0]].x < lm[pip[0]].x)  # thumb
    for t, p in zip(tips[1:], pip[1:]):
        fingers.append(lm[t].y < lm[p].y)
    return fingers

def mouth_open(face_landmarks):
    lm = face_landmarks.landmark
    top_lip = lm[13]
    bottom_lip = lm[14]
    return (bottom_lip.y - top_lip.y) * 1000 > 20

def eyebrows_raised(face_landmarks):
    lm = face_landmarks.landmark
    left_eyebrow = lm[65].y
    left_eye = lm[159].y
    right_eyebrow = lm[295].y
    right_eye = lm[386].y
    return (left_eye - left_eyebrow > 5e-2) or (right_eye - right_eyebrow > 5e-2)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Hand detection
    hand_result = hands.process(frame_rgb)
    gesture_name = "base"

    if hand_result.multi_hand_landmarks:
        for hand_landmarks in hand_result.multi_hand_landmarks:
            fingers = fingers_up(hand_landmarks)
            if fingers == [1,1,1,1,1]: gesture_name = "🖐"
            elif fingers == [0,1,1,0,0]: gesture_name = "✌️"
            elif fingers == [0,1,1,1,0]: gesture_name = "🤟"
            elif fingers == [0,1,0,0,0]: gesture_name = "☝️"
            elif fingers == [0,0,0,0,0]: gesture_name = "✊"
            elif fingers == [1,1,0,0,0]: gesture_name = "🤞"
            else: gesture_name = "base"

            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Face detection
    face_result = face_mesh.process(frame_rgb)
    mouth_open_flag = False
    eyebrows_flag = False
    wink_flag = None
    smile_flag = False

    if face_result.multi_face_landmarks:
        for face_landmarks in face_result.multi_face_landmarks:
            mouth_open_flag = mouth_open(face_landmarks)
            eyebrows_flag = eyebrows_raised(face_landmarks)

            mp_draw.draw_landmarks(frame, face_landmarks, mp_face.FACEMESH_TESSELATION)

    # PRIORITY: mouth open → eyebrows → gestures
    if mouth_open_flag:
        current_img = images["a"].copy()
    elif eyebrows_flag:
        current_img = images["b"].copy()
    else:
        if gesture_name == "🖐": current_img = images["c"].copy()
        elif gesture_name == "☝️": current_img = images["e"].copy()
        elif gesture_name == "✊": current_img = images["f"].copy()
        elif gesture_name == "🤞": current_img = images["g"].copy()
        else: current_img = images["base"].copy()

    # Show webcam and meme image
    cv2.imshow("Webcam", frame)
    cv2.imshow("Meme", current_img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
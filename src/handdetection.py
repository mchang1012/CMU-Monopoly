import cv2
import mediapipe as mp
#from mediapipe handslibrary
drawing = mp.solutions.drawing_utils
drawingStyles = mp.solutions.drawing_styles
handsSol = mp.solutions.hands

handsProcessor = handsSol.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

#coded below on own referencing mediapipe library
fingerTips = [4,8,12,16,20]
fingerPips = [3,6,10,14,18]
#counts number of fingers
def countFingers(landmarks, whichHand):
    count = 0
    if whichHand == 'Right':
        if landmarks[fingerTips[0]].x < landmarks[fingerPips[0]].x:
            count += 1
    else: 
        if landmarks[fingerTips[0]].x > landmarks[fingerPips[0]].x:
            count += 1
    for i in range (1, len(fingerTips)):
        tip = fingerTips[i]
        pip = fingerPips[i]
        if landmarks[tip].y < landmarks[pip].y:
            count += 1
    return count
#used chatGPT 
#gets information to feed into counting fingers
def detectFingers(frame):
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = handsProcessor.process(image)
    if not results.multi_hand_landmarks:
        return 0
    landmarks = results.multi_hand_landmarks[0].landmark
    whichHand = results.multi_handedness[0].classification[0].label
    return countFingers(landmarks, whichHand)
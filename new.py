
import cv2
import mediapipe as mp
import serial

# Initialize the Arduino serial connection
ser = serial.Serial('/dev/cu.usbserial-10', 9600)  # Replace 'COM3' with the appropriate serial port for your Arduino

# Initialize the Mediapipe Hand tracking module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8)

# Open the webcam video stream
video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    frame = cv2.flip(frame, 1)

    # Convert the frame to RGB for Mediapipe
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with Mediapipe
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get the position of the thumb tip
            thumb_tip = hand_landmarks.landmark[4]
            thumb_tip_y = int(thumb_tip.y * frame.shape[0])

            # Check if the thumb tip is above the midpoint of the frame
            if thumb_tip_y < frame.shape[0] // 2:
                ser.write(b'1')  # Send command to turn the LED on
            else:
                ser.write(b'0')  # Send command to turn the LED off

    # Display the frame
    cv2.imshow("frame", frame)
    k = cv2.waitKey(1)
    if k == ord("k"):
        break

# Release video capture and close all windows
video.release()
cv2.destroyAllWindows()

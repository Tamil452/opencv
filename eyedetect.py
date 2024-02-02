import numpy as np
import cv2
import dlib

cap = cv2.VideoCapture(0)

# Load facial landmarks predictor
predictor_path = "path/to/shape_predictor_68_face_landmarks.dat"  # You need to download this file
predictor = dlib.shape_predictor(predictor_path)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        # Extract facial landmarks
        rect = dlib.rectangle(int(x), int(y), int(x + w), int(y + h))
        landmarks = predictor(gray, rect)

        # Get coordinates of the left and right eyes
        left_eye_coords = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(36, 42)]
        right_eye_coords = [(landmarks.part(i).x, landmarks.part(i).y) for i in range(42, 48)]

        # Draw rectangles around eyes
        cv2.polylines(frame, [np.array(left_eye_coords)], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.polylines(frame, [np.array(right_eye_coords)], isClosed=True, color=(0, 255, 0), thickness=2)

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

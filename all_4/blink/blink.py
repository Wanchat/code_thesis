from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import text


def eye_aspect_ratio(eye):
    #EAR
    P2_P6 = dist.euclidean(eye[1], eye[5])
    P3_P5 = dist.euclidean(eye[2], eye[4])
    P1_P4 = dist.euclidean(eye[0], eye[3])
    ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
    return ear

BLINK_LESS = 0.27
BLINK_FRAMES = .22

COUNTER = 0
TOTAL = 0
ear =0
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(r'D:\code_thesis\code_thesis\shape_predictor_68_face_landmarks.dat')
# indexes facial landmarks
(l_Start, l_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_Start, r_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

cap = cv2.VideoCapture(0)

# ---------------------------------------------------------------------
while True:
    success, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects:
        #detect & convert np
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        #extend for def eye aspect ratio
        leftEye = shape[l_Start:l_End]
        rightEye = shape[r_Start:r_End]

        # rightEye
        rx_0, ry_0 = rightEye[0]
        rx_1, ry_1 = rightEye[1]
        rx_2, ry_2 = rightEye[2]
        rx_3, ry_3 = rightEye[3]
        rx_4, ry_4 = rightEye[4]
        rx_5, ry_5 = rightEye[5]

        # leftEye
        lx_0, ly_0 = leftEye[0]
        lx_1, ly_1 = leftEye[1]

        lx_2, ly_2 = leftEye[2]
        lx_3, ly_3 = leftEye[3]
        lx_4, ly_4 = leftEye[4]
        lx_5, ly_5 = leftEye[5]

        #use def def eye aspect ratio
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        # average EAR two eye
        ear = (leftEAR + rightEAR) / 2.0

        # vertor to draw & draw


        # cv2.line(frame, (lx_0,ly_0), (lx_3,ly_3), (0,255,0), 1)
        # cv2.line(frame, (lx_1,ly_1), (lx_5,ly_5), (0,255,0), 1)
        # cv2.line(frame, (lx_2,ly_2), (lx_4,ly_4), (0,255,0), 1)

        for (x, y) in (rightEye):
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        for (x, y) in (leftEye):
            cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

        # leftEyeHull = cv2.convexHull(leftEye)
        # rightEyeHull = cv2.convexHull(rightEye)
        # cv2.drawContours(frame, [leftEyeHull], -1, (255, 255, 255), 1)
        # cv2.drawContours(frame, [rightEyeHull], -1, (255, 255, 255), 1)

        # check EAR < blink_less
        if ear < BLINK_LESS:
            COUNTER += 1
        else:
            # check frame blink
            if COUNTER >= BLINK_FRAMES:
                TOTAL += 1
                print(TOTAL)
            # reset frame blink
            COUNTER = 0
    overlay = frame.copy()
    cv2.rectangle(overlay, (255, 430), (385, 470), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, frame, 1 - 0.6, 0, frame)
    cv2.rectangle(frame,(255,430),(385,470),(0,0,0),1)

    # cv2.line(frame,(320,430),(320,470),(0,0,0),1)
    # cv2.putText(frame, "Blinks: {}".format(TOTAL), (190, 460),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)
    # cv2.putText(frame, "EAR: {:.2f}".format(ear), (352, 460),
    #             cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1)

    fontpath = "Prompt-Regular.ttf"
    frame = text.text(frame, (270, 435), fontpath, "Blinks: {}".format(TOTAL), 23, (0,255,0))

    # frame = text.text(frame, (193, 440), fontpath, "Blinks: {}".format(TOTAL), 23, (0,255,0))
    # frame = text.text(frame, (352, 440), fontpath, "EAR: {:.2f}".format(ear).format(TOTAL), 23, (0,255,0))

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

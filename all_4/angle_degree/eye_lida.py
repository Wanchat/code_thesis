
from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
from detect_angle_lida import line_angle
import log
import text

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# indexes facial landmarks
(l_Start, l_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_Start, r_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

cap = cv2.VideoCapture(0)

num_frame = 0
log_angle = []
stop = ""

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

        rx_1, ry_1 = rightEye[0]
        rx_2, ry_2 = rightEye[3]

        lx_1, ly_1 = leftEye[0]
        lx_2, ly_2 = leftEye[3]

        rx = (rx_2 - rx_1)/2
        ry = (ry_2 - ry_1)/2

        lx = (lx_2 - lx_1)/2
        ly = (ly_2 - ly_1)/2

        rx = int(rx)
        ry = int(ry)

        lx = int(lx)
        ly = int(ly)

        # draw vector
        cv2.circle(frame, (rx_1+rx, ry_1+ry), 2, (0,255,0), -1)
        cv2.circle(frame, (lx_1+rx, ly_1+ry), 2, (0,255,0), -1)
        cv2.line(frame, (rx_1+rx, ry_1+ry), (lx_1+rx, ly_1+ry), (0,255,0), 1)

        cx = ((rx_1 + rx) + (lx_1 + rx))/2
        cy = ((ry_1 + ry) + (ly_1 + ry))/2

        cx = int(cx)
        cy = int(cy)

        cv2.circle(frame, (cx, cy), 4, (0,255,0), -1)

        eye_y = ((ry_1+ry)+(ly_1+ry))/2

        degree = line_angle(eye_y)

        print ("angle : {}".format(degree))

        # text
        pathfont = "Prompt-Regular.ttf"
        roi = (20, 20)
        frame = text.text(frame, roi, pathfont, str("angle: {}".format(degree)) ,24 ,(0, 255, 0))

        # number frame
        num_frame += 1

        # add list
        if num_frame != 11:
            log_angle.append(degree)

        else:
            print("[INFO] >>>>>>> save log")
            stop = "q"
            break

    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) and stop == "q":
    # if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print(log_angle)

# add plot and add csv
log.csv_log(log_angle, "angle_log")

try:
    log.plot_log(log_angle)
except:
    pass
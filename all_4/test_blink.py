from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
def blink():
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
    predictor = dlib.shape_predictor('/home/wanchat/Python/data/'
                                     'shape_predictor_68_face_landmarks.dat')
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

            #use def def eye aspect ratio
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)

            # average EAR two eye
            ear = (leftEAR + rightEAR) / 2.0

            # vertor to draw & draw
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (255, 255, 255), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (255, 255, 255), 1)

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
        cv2.rectangle(overlay, (160, 430), (480, 470), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 1 - 0.6, 0, frame)

        cv2.rectangle(frame,(160,430),(480,470),(0,0,0),1)
        cv2.line(frame,(320,430),(320,470),(0,0,0),1)

        fontpath = "/home/wanchat/Python/data/font/Roboto/Roboto-Medium.ttf"
        font = ImageFont.truetype(fontpath, 23)
        img_pil = Image.fromarray(frame)
        draw = ImageDraw.Draw(img_pil)
        draw.text((193, 440), "Blinks: {}".format(TOTAL), font=font, fill=(0, 255, 0, 0))
        draw.text((352, 440),  "EAR: {:.2f}".format(ear), font=font, fill=(0, 255, 0, 0))
        frame = np.array(img_pil)

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    blink()

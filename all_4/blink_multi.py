from scipy.spatial import distance as dist
from imutils import face_utils
import dlib
import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import argparse

def EAR(eye):
    P2_P6 = dist.euclidean(eye[1],eye[5])
    P3_P5 = dist.euclidean(eye[2],eye[4])
    P1_P4 = dist.euclidean(eye[0],eye[3])
    ear = (P2_P6 + P3_P5) / (2.0 * P1_P4)
    return ear

BLINK_LESS = 0.27
BLINK_FRAMES = 2.2

COUNTER = 0
TOTAL = 0
ear =0

ad = argparse.ArgumentParser()
ad.add_argument('--camera', type = int)
args = vars(ad.parse_args())


detector = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor('/home/wanchat/Python/data/'
                               'shape_predictor_68_face_landmarks.dat')

# camera = int(input('camera : '))

cap = cv2.VideoCapture(args['camera'])
window = np.zeros((480,880,3),np.uint8)
while True:
    success, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = detector(gray, 0)

    for rect in rects: #for predict
        face = predict(gray, rect)
        face = face_utils.shape_to_np(face)

        face_idex = []
        #loop  index face
        for (x,y) in face:
            face_idex.append((x,y))
        leftEye = face_idex[36:42]
        rightEye = face_idex[42:48]
        #use def ear
        left_EAR = EAR(leftEye)
        right_EAR = EAR(rightEye)
        ear = (left_EAR + right_EAR) / 2.0
        #resiz face
        cub_0x, cub_0y = face_idex[0]
        cub_19x, cub_19y = face_idex[19]
        cub_8x, cub_8y = face_idex[8]
        cub_16x, cub_16y = face_idex[16]
        face_crop = frame[cub_19y:cub_8y, cub_0x:cub_16x ]
        #resize left eye
        rec1_x, rec1_y = leftEye[0]
        rec2_x, rec2_y = leftEye[1]
        rec3_x, rec3_y = leftEye[3]
        rec4_x, rec4_y = leftEye[4]
        eye_re_1 = frame[rec2_y - 15: rec4_y + 15, rec1_x - 10: rec3_x + 10]
        #resize right eye
        rec5_x, rec5_y = rightEye[0]
        rec6_x, rec6_y = rightEye[1]
        rec7_x, rec7_y = rightEye[3]
        rec8_x, rec8_y = rightEye[4]
        eye_re_2 = frame[rec6_y - 15: rec8_y + 15, rec5_x - 10: rec7_x + 10]

        try:
            eye_resize_1 = cv2.resize(eye_re_1, (240, 120))
            window[240:360, 640:880] = eye_resize_1
            eye_resize_2 = cv2.resize(eye_re_2, (240, 120))
            window[360:480, 640:880] = eye_resize_2
            re_face = cv2.resize(face_crop, (240, 240))
            window[0:240, 640:880] = re_face
        except:
            continue
        # draw eye
        pts = np.array([leftEye[0], leftEye[1],
                        leftEye[2], leftEye[3],
                        leftEye[4], leftEye[5]], np.int64)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 255, 255), 1)
        pts = np.array([rightEye[0], rightEye[1],
                        rightEye[2], rightEye[3],
                        rightEye[4], rightEye[5]], np.int64)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(frame, [pts], True, (255, 255, 255), 1)
        #draw face
        cv2.rectangle(frame,(cub_0x,cub_19y),(cub_16x,cub_8y),(255,255,255),1)

        if ear < BLINK_LESS:
            COUNTER +=1
        else:
           if COUNTER >= BLINK_FRAMES:
               TOTAL += 1
           COUNTER = 0

    overlay = frame.copy()
    cv2.rectangle(overlay, (160, 430), (480, 470), (0, 0, 0), -1)
    cv2.addWeighted(overlay, 0.6, frame, 1 - 0.6, 0, frame)

    overlay_2 = window.copy()
    cv2.rectangle(overlay_2, (640,210), (695,240), (0, 0, 0), -1)
    cv2.rectangle(overlay_2, (640,330), (715,360), (0, 0, 0), -1)
    cv2.rectangle(overlay_2, (640,450), (720,480), (0, 0, 0), -1)

    cv2.addWeighted(overlay_2, 0.6, window, 1 - 0.6, 0, window)

    cv2.line(frame,(320,430),(320,470),(0,0,0),1)

    #text
    fontpath = "/home/wanchat/Python/data/font/Roboto/Roboto-Medium.ttf"
    font = ImageFont.truetype(fontpath, 23)
    font_2 = ImageFont.truetype(fontpath, 16)

    img_pil = Image.fromarray(frame)
    draw = ImageDraw.Draw(img_pil)
    draw.text((193, 440), "Blinks: {}".format(TOTAL), font=font, fill=(0, 255, 0, 0))
    draw.text((352, 440),  "EAR: {:.2f}".format(ear), font=font, fill=(0, 255, 0, 0))
    frame = np.array(img_pil)

    img_pil2 = Image.fromarray(window)
    draw = ImageDraw.Draw(img_pil2)
    draw.text((650, 215),  "face", font=font_2, fill=(0, 255, 0, 0))
    draw.text((650, 335),  "eye left", font=font_2, fill=(0, 255, 0, 0))
    draw.text((650, 455),  "eye right", font=font_2, fill=(0, 255, 0, 0))
    window = np.array(img_pil2)

    cv2.line(window,(640,0),(640,480),(0,0,0),1)
    cv2.line(window,(640,240),(880,240),(0,0,0),1)
    cv2.line(window,(640,360),(880,360),(0,0,0),1)
    cv2.rectangle(window,(1,1),(879,479),(0,0,0),1)
    cv2.rectangle(frame,(1,1),(640,479),(0,0,0),1)

    window[0:480,0:640] = frame
    cv2.imshow("Frame", window)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()

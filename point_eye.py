from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('/home/wanchat/data_python/model/shape_predictor_68_face_landmarks.dat')

cap = cv2.VideoCapture(0)

while True:

	rect, frame = cap.read()

	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	rects = detector(gray, 1)

	

	for (i, rect) in enumerate(rects):
	    shape = predictor(gray, rect)
	    shape = face_utils.shape_to_np(shape)
	    (x, y, w, h) = face_utils.rect_to_bb(rect)
	    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		for n, (xx, yy) in enumerate(shape):
			# xy.append((xx, yy))
			cv2.circle (frame, (xx, yy), 1, (0, 0, 255), -1)

    # eyeLeft
    # eyeLeft = xy[22], xy[23], xy[26], xy[46]
    # eyeLeft_1, eyeLeft_2, eyeLeft_3, eyeLeft_4 = eyeLeft

    # eyeLeft_1_x, eyeLeft_1_y = eyeLeft_1
    # eyeLeft_2_x, eyeLeft_2_y = eyeLeft_2
    # eyeLeft_3_x, eyeLeft_3_y = eyeLeft_3
    # eyeLeft_4_x, eyeLeft_4_y = eyeLeft_4

    # cv2.line(frame, xy[36], xy[39], (0, 255, 0), 1)
    # cv2.line(frame, xy[42], xy[45], (0, 255, 0), 1)

    # eyeRight
    # eyeRight =  xy[17], xy[19], xy[21], xy[40]
    # eyeRight_1, eyeRight_2, eyeRight_3, eyeRight_4 = eyeRight

    # eyeRight_1_x, eyeRight_1_y = eyeRight_1
    # eyeRight_2_x, eyeRight_2_y = eyeRight_2
    # eyeRight_3_x, eyeRight_3_y = eyeRight_3
    # eyeRight_4_x, eyeRight_4_y = eyeRight_4


	cv2.imshow("Output", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
# import the necessary packages
from imutils import face_utils
import numpy as np
import argparse
import imutils
import dlib
import cv2

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('/home/wanchat/data_python/model'
							'/shape_predictor_68_face_landmarks.dat')

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

		cv2.circle (frame, (xx, yy), 1, (0, 0, 255), -1)


	cv2.imshow("Output", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destroyAllWindows()
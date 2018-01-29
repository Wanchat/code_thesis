import numpy as np
import cv2
cap = cv2.VideoCapture(0)
eye_cascade = cv2.CascadeClassifier('/home/wanchat/Python/opencv/data/haarcascade_eye.xml')
face_cascade = cv2.CascadeClassifier('/home/wanchat/Python/opencv/data/haarcascade_frontalface_default.xml')
while (True):
    ok,frame = cap.read()
    glay = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    eye = eye_cascade.detectMultiScale(glay,1.3,5)
    face = face_cascade.detectMultiScale(glay,1.3,5)
    # global x, y, w, h

    for (x,y,w,h) in face:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),2)
        cv2.rectangle(frame, (x-1, y + h), (x + w+1, y + h + 30), (255, 255, 255), -1)

    # องศาตามมุมกล้อง
    l = (0, 13.861, 27.904, 41.807, 55.58, 69.234, 82.779, 96.223, 109.577,
          122.848, 136.046, 149.18, 162.258, 175.287, 188.277, 201.236, 214.17,
          227.089, 240, 252.911, 265.83, 278.764, 291.723, 304.713, 317.742, 330.82,
          343.954 , 357.152, 370.423, 383.777, 397.221, 410.766, 424.42, 438.193,
          452.096, 466.139, 480)

    # เส้นองศามุมกล้อง
    for line_an in l:
        cv2.line(frame, (0, np.int(line_an)), (640, np.int(line_an)), (0, 255, 255), 1)
    # vector rect and circle eye
    for (ex,ey,ew,eh) in eye:
        center_x = np.float(ex + (ew * 0.5))
        center_y = np.float(ey + (eh * 0.5))

        # print(center_x, center_y)

        center_xx = np.int(center_x)
        center_yy = np.int(center_y)

        color = (0,0,0)
        under = (0,0,255)
        on = (255,0,0)

        if center_y > 240:
            color = under
        else:
            color = on

        cv2.circle(frame, (center_xx, center_yy), 5, (color), -1)

        angle = 0

        if center_y >= l[0]and center_y < l[1] :
            angle = 18
        elif center_y >= l[1]and center_y < l[2] :
            angle = 17
        elif center_y >= l[2]and center_y < l[3] :
            angle = 16
        elif center_y >= l[3]and center_y < l[4] :
            angle = 15
        elif center_y >= l[4]and center_y < l[5] :
            angle = 14
        elif center_y >= l[5]and center_y < l[6] :
            angle = 13
        elif center_y >= l[6]and center_y < l[7] :
            angle = 12
        elif center_y >= l[7]and center_y < l[8] :
            angle = 11
        elif center_y >= l[8]and center_y < l[9] :
            angle = 10
        elif center_y >= l[9]and center_y < l[10] :
            angle = 9
        elif center_y >= l[10]and center_y < l[11] :
            angle = 8
        elif center_y >= l[11]and center_y < l[12] :
            angle = 7
        elif center_y >= l[12]and center_y < l[13] :
            angle = 6
        elif center_y >= l[13]and center_y < l[12] :
            angle = 5
        elif center_y >= l[14]and center_y < l[15] :
            angle = 4
        elif center_y >= l[15]and center_y < l[16] :
            angle = 3
        elif center_y >= l[16]and center_y < l[17] :
            angle = 2
        elif center_y >= l[17]and center_y < l[18] :
            angle = 1
        elif center_y >= l[18]and center_y < l[19] :
            angle = 0
        elif center_y >= l[19]and center_y < l[20] :
            angle = 1
        elif center_y >= l[20]and center_y < l[21] :
            angle = 2
        elif center_y >= l[22]and center_y < l[23] :
            angle = 3
        elif center_y >= l[23]and center_y < l[24] :
            angle = 4
        elif center_y >= l[24]and center_y < l[25] :
            angle = 5
        elif center_y >= l[25]and center_y < l[26] :
            angle = 6
        elif center_y >= l[26]and center_y < l[27] :
            angle = 7
        elif center_y >= l[27]and center_y < l[28] :
            angle = 8
        elif center_y >= l[28]and center_y < l[29] :
            angle = 9
        elif center_y >= l[29]and center_y < l[30] :
            angle = 10
        elif center_y >= l[30]and center_y < l[31] :
            angle = 11
        elif center_y >= l[31]and center_y < l[32] :
            angle = 12
        elif center_y >= l[32]and center_y < l[33] :
            angle = 13
        elif center_y >= l[33]and center_y < l[34] :
            angle = 14
        elif center_y >= l[34]and center_y < l[35] :
            angle = 15
        elif center_y >= l[35]and center_y < l[36] :
            angle = 16
        elif center_y >= l[35]and center_y < l[36] :
            angle = 17
        elif center_y >= l[35]and center_y < l[36] :
            angle = 18
        else:
            angle = "not detect angle"

        font = cv2.FONT_HERSHEY_DUPLEX

        if center_y > 240:
            cv2.putText(frame,"under", (15, 240), font, np.float(1), (0, 0, 250), 1)
            text3 = 'UNDER'
        else:
            cv2.putText(frame, "on", (15, 240), font, np.float(1), (250, 0, 0), 1)
            text3 = 'ON'

        text = str(angle)
        text2 = "degree: " + text + " : "+ text3

        cv2.putText(frame, str(text2), (x+3, y+h+22), font, np.float(0.6), (color), 1)
        print("degree: ",angle)

    cv2.imshow('VIDEO',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

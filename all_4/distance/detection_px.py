import numpy as np
import cv2
import log
import text

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

log_cm = []
num_frame = 0
stop = ""

while (True):
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    px = [pixel for pixel in range(330,125,-3)]

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0,255,0), 2)
        high = (y+h)-y
        distance = 0
        start = 30

        if high >= 333 < 480:
            distance = "less 30"
        elif high >=px[1] < 333:
            distance = start+1
        elif high >=px[2] < px[1]:
            distance = start+2
        elif high >=px[3] < px[2]:
            distance = start + 3
        elif high >=px[4] < px[3]:
            distance = start+4
        elif high >=px[5] < px[4]:
            distance = start+5
        elif high >=px[6] < px[5]:
            distance = start+6
        elif high >=px[7] < px[6]:
            distance = start+7
        elif high >=px[8] < px[7]:
            distance = start+8
        elif high >=px[9] < px[8]:
            distance = start+8
        elif high >=px[10] < px[9]:
            distance = start+10
        elif high >=px[11] < px[10] :
            distance = start+11
        elif high >=px[12] < px[11]:
            distance = start+12
        elif high >=px[13] < px[12]:
            distance = start+13
        elif high >=px[14] < px[13]:
            distance = start+14
        elif high >=px[15] < px[14]:
            distance = start+15
        elif high >=px[16] < px[15]:
            distance = start+16
        elif high >=px[17] < px[16]:
            distance = start+17
        elif high >=px[18] < px[17]:
            distance = start+18
        elif high >=px[19] < px[18]:
            distance = start+19
        elif high >=px[20] < px[19]:
            distance = start+20
        elif high >=px[21] < px[20]:
            distance = start+21
        elif high >=px[22] < px[21]:
            distance = start+22
        elif high >=px[23] < px[22] :
            distance = start+23
        elif high >=px[24] < px[23]:
            distance = start+24
        elif high >=px[25] < px[24]:
            distance = start+25
        elif high >=px[26] < px[25]:
            distance = start+26
        elif high >=px[27] < px[26]:
            distance = start+27
        elif high >=px[28] < px[27]:
            distance = start+28
        elif high >=px[29] < px[28]:
            distance = start+29
        elif high >=px[30] < px[29]:
            distance = start+30
        elif high >=px[31] < px[30]:
            distance = start+31
        elif high >=px[32] < px[31]:
            distance = start+32
        elif high >=px[33] < px[32]:
            distance = start+33
        elif high >=px[34] < px[33]:
            distance = start+34
        elif high >=px[35] < px[34]:
            distance = start+35
        elif high >=px[36] < px[35]:
            distance = start+36
        elif high >=px[37] < px[26]:
            distance = start+37
        elif high >=px[38] < px[37]:
            distance = start+38
        elif high >=px[39] < px[38]:
            distance = start+39
        elif high >=px[40] < px[39]:
            distance = start+40
        elif high >=px[41] < px[40]:
            distance = start+41
        elif high >=px[42] < px[41]:
            distance = start+42
        elif high >=px[43] < px[42]:
            distance = start+43
        elif high >=px[43] < px[43]:
            distance = start+2
        elif high >=px[44] < px[43]:
            distance = start+44
        elif high >=px[45] < px[44] :
            distance = start+45
        elif high >=px[46] < px[45]:
            distance = start+46
        elif high >=px[47] < px[46]:
            distance = start+2
        elif high >=px[48] < px[47]:
            distance = start+48
        elif high >=px[49] < px[48]:
            distance = start+49
        elif high >=px[50] < px[49]:
            distance = start+50
        elif high >=px[51] < px[50]:
            distance = start+51
        elif high >=px[52] < px[51]:
            distance = start+52
        elif high >=px[53] < px[52]:
            distance = start+53
        elif high >=px[54] < px[53]:
            distance = start+54
        elif high >=px[55] < px[54]:
            distance = start+55
        elif high >=px[56] < px[55]:
            distance = start+56
        elif high >=px[57] < px[56]:
            distance = start+57
        elif high >=px[58] < px[57]:
            distance = start+58
        elif high >=px[59] < px[58]:
            distance = start+59
        elif high >=px[60] < px[59]:
            distance = start+60
        elif high >=px[61] < px[60]:
            distance = start+61
        elif high >=px[62] < px[61]:
            distance = start+62
        elif high >=px[63] < px[62]:
            distance = start+63
        elif high >=px[64] < px[63]:
            distance = start+64
        elif high >=px[65] < px[64]:
            distance = start+65
        elif high >=px[66] < px[65]:
            distance = start+65
        elif high >=px[67] < px[66]:
            distance = start+67
        elif high >=px[68] < px[67]:
            distance = start + 68
        elif high >=   123 < px[68]:
            distance = start + 69
        else:
            distance = 'over 100'

        print('distance: ', distance,' cm')

        log_cm.append(distance)

        # text
        pathfont = "Prompt-Regular.ttf"
        roi = (20, 20)
        img = text.text(img, roi, pathfont, str("distance:{} cm").format(distance) ,24 ,(0, 255, 0))

        if num_frame != 10:
            num_frame += 1
        else:
            print("[INFO] >>>>>>> save log")
            stop = "q"
            break


    cv2.imshow('frame', img)
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    if cv2.waitKey(1) and stop == "q":
        break

cap.release()
cv2.destroyAllWindows()

print(log_cm)

# add plot and add csv
log.csv_log(log_cm, "distance_log")

try:
    log.plot_log(log_cm)
except:
    pass
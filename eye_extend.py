from imutils import face_utils

(l_Start, l_End) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(r_Start, r_End) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

def extend(shape):
    rightEye = shape[r_Start:r_End]
    leftEye = shape[l_Start:l_End]

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
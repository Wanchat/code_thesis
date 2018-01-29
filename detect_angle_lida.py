import numpy as np

def line_angle(x):

	angle_line_np = np.arange(0, 240, 13.33)
	angle_litda_18 = np.arange(angle_line_np[0], angle_line_np[1], 1.33)
	angle_litda_17 = np.arange(angle_line_np[1], angle_line_np[2], 1.33)
	angle_litda_16 = np.arange(angle_line_np[2], angle_line_np[3], 1.33)
	angle_litda_15 = np.arange(angle_line_np[3], angle_line_np[4], 1.33)
	angle_litda_14 = np.arange(angle_line_np[4], angle_line_np[5], 1.33)
	angle_litda_13 = np.arange(angle_line_np[5], angle_line_np[6], 1.33)
	angle_litda_12 = np.arange(angle_line_np[6], angle_line_np[7], 1.33)
	angle_litda_11 = np.arange(angle_line_np[7], angle_line_np[8], 1.33)
	angle_litda_10 = np.arange(angle_line_np[8], angle_line_np[9], 1.33)
	angle_litda_9 = np.arange(angle_line_np[9], angle_line_np[10], 1.33)
	angle_litda_8 = np.arange(angle_line_np[10], angle_line_np[11], 1.33)
	angle_litda_7 = np.arange(angle_line_np[11], angle_line_np[12], 1.33)
	angle_litda_6 = np.arange(angle_line_np[12], angle_line_np[13], 1.33)
	angle_litda_5 = np.arange(angle_line_np[13], angle_line_np[14], 1.33)
	angle_litda_4 = np.arange(angle_line_np[14], angle_line_np[15], 1.33)
	angle_litda_3 = np.arange(angle_line_np[15], angle_line_np[16], 1.33)
	angle_litda_2 = np.arange(angle_line_np[16], angle_line_np[17], 1.33)
	angle_litda_1 = np.arange(angle_line_np[17], 240, 1.33)

	angle_line2_np = np.arange(240, 480, 13.33)
	angle_litda2_1 = np.arange(angle_line2_np[0], angle_line2_np[1], 1.33)
	angle_litda2_2 = np.arange(angle_line2_np[1], angle_line2_np[2], 1.33)
	angle_litda2_3 = np.arange(angle_line2_np[2], angle_line2_np[3], 1.33)
	angle_litda2_4 = np.arange(angle_line2_np[3], angle_line2_np[4], 1.33)
	angle_litda2_5 = np.arange(angle_line2_np[4], angle_line2_np[5], 1.33)
	angle_litda2_6 = np.arange(angle_line2_np[5], angle_line2_np[6], 1.33)
	angle_litda2_7 = np.arange(angle_line2_np[6], angle_line2_np[7], 1.33)
	angle_litda2_8 = np.arange(angle_line2_np[7], angle_line2_np[8], 1.33)
	angle_litda2_9 = np.arange(angle_line2_np[8], angle_line2_np[9], 1.33)
	angle_litda2_10 = np.arange(angle_line2_np[9], angle_line2_np[10], 1.33)
	angle_litda2_11 = np.arange(angle_line2_np[10],angle_line2_np[11], 1.33)
	angle_litda2_12= np.arange(angle_line2_np[11], angle_line2_np[12], 1.33)
	angle_litda2_13 = np.arange(angle_line2_np[12], angle_line2_np[13], 1.33)
	angle_litda2_14 = np.arange(angle_line2_np[13], angle_line2_np[14], 1.33)
	angle_litda2_15 = np.arange(angle_line2_np[14], angle_line2_np[15], 1.33)
	angle_litda2_16 = np.arange(angle_line2_np[15], angle_line2_np[16], 1.33)
	angle_litda2_17 = np.arange(angle_line2_np[16], angle_line2_np[17], 1.33)
	angle_litda2_18 = np.arange(angle_line2_np[17], 480, 1.33)

	#18
	if x > angle_litda_18[0] and x <= angle_litda_18[1]:
		x = 18
	elif x > angle_litda_18[1] and x <= angle_litda_18[2]:
		x = 17 + 0.9 
	elif x > angle_litda_18[2] and x <= angle_litda_18[3]:
		x = 17 + 0.8 
	elif x > angle_litda_18[3] and x <= angle_litda_18[4]:
		x = 17 + 0.7 
	elif x > angle_litda_18[4] and x <= angle_litda_18[5]:
		x = 17 + 0.6 
	elif x > angle_litda_18[5] and x <= angle_litda_18[6]:
		x = 17 + 0.5 
	elif x > angle_litda_18[6] and x <= angle_litda_18[7]:
		x = 17 + 0.4
	elif x > angle_litda_18[7] and x <= angle_litda_18[8]:
		x = 17 + 0.3
	elif x > angle_litda_18[8] and x <= angle_litda_18[9]:
		x = 17 + 0.2		
	elif x > angle_litda_18[9] and x <= angle_litda_17[0]:
		x = 17 + 0.1

	#17
	elif x > angle_litda_17[0] and x <= angle_litda_17[1]:
		x = 17
	elif x > angle_litda_17[1] and x <= angle_litda_17[2]:
		x = 16 + 0.9 
	elif x > angle_litda_17[2] and x <= angle_litda_17[3]:
		x = 16 + 0.8 
	elif x > angle_litda_17[3] and x <= angle_litda_17[4]:
		x = 16 + 0.7 
	elif x > angle_litda_17[4] and x <= angle_litda_17[5]:
		x = 16 + 0.6 
	elif x > angle_litda_17[5] and x <= angle_litda_17[6]:
		x = 16 + 0.5 
	elif x > angle_litda_17[6] and x <= angle_litda_17[7]:
		x = 16 + 0.4
	elif x > angle_litda_17[7] and x <= angle_litda_17[8]:
		x = 16 + 0.3
	elif x > angle_litda_17[8] and x <= angle_litda_17[9]:
		x = 16 + 0.2		
	elif x > angle_litda_17[9] and x <= angle_litda_16[0]:
		x = 16 + 0.1	
	
	#16
	elif x > angle_litda_16[0] and x <= angle_litda_16[1]:
		x = 16
	elif x > angle_litda_16[1] and x <= angle_litda_16[2]:
		x = 15 + 0.9 
	elif x > angle_litda_16[2] and x <= angle_litda_16[3]:
		x = 15 + 0.8 
	elif x > angle_litda_16[3] and x <= angle_litda_16[4]:
		x = 15 + 0.7 
	elif x > angle_litda_16[4] and x <= angle_litda_16[5]:
		x = 15 + 0.6 
	elif x > angle_litda_16[5] and x <= angle_litda_16[6]:
		x = 15 + 0.5 
	elif x > angle_litda_16[6] and x <= angle_litda_16[7]:
		x = 15 + 0.4
	elif x > angle_litda_16[7] and x <= angle_litda_16[8]:
		x = 15 + 0.3
	elif x > angle_litda_16[8] and x <= angle_litda_16[9]:
		x = 15 + 0.2		
	elif x > angle_litda_16[9] and x <= angle_litda_15[0]:
		x = 15 + 0.1

	#15
	elif x > angle_litda_15[0] and x <= angle_litda_15[1]:
		x = 15
	elif x > angle_litda_15[1] and x <= angle_litda_15[2]:
		x = 14 + 0.9 
	elif x > angle_litda_15[2] and x <= angle_litda_15[3]:
		x = 14 + 0.8 
	elif x > angle_litda_15[3] and x <= angle_litda_15[4]:
		x = 14 + 0.7 
	elif x > angle_litda_15[4] and x <= angle_litda_15[5]:
		x = 14 + 0.6 
	elif x > angle_litda_15[5] and x <= angle_litda_15[6]:
		x = 14 + 0.5 
	elif x > angle_litda_15[6] and x <= angle_litda_15[7]:
		x = 14 + 0.4
	elif x > angle_litda_15[7] and x <= angle_litda_15[8]:
		x = 14 + 0.3
	elif x > angle_litda_15[8] and x <= angle_litda_15[9]:
		x = 14 + 0.2		
	elif x > angle_litda_15[9] and x <= angle_litda_14[0]:
		x = 14 + 0.1

	#14
	elif x > angle_litda_14[0] and x <= angle_litda_14[1]:
		x = 14
	elif x > angle_litda_14[1] and x <= angle_litda_14[2]:
		x = 13 + 0.9 
	elif x > angle_litda_14[2] and x <= angle_litda_14[3]:
		x = 13 + 0.8 
	elif x > angle_litda_14[3] and x <= angle_litda_14[4]:
		x = 13 + 0.7 
	elif x > angle_litda_14[4] and x <= angle_litda_14[5]:
		x = 13 + 0.6 
	elif x > angle_litda_14[5] and x <= angle_litda_14[6]:
		x = 13 + 0.5 
	elif x > angle_litda_14[6] and x <= angle_litda_14[7]:
		x = 13 + 0.4
	elif x > angle_litda_14[7] and x <= angle_litda_14[8]:
		x = 13 + 0.3
	elif x > angle_litda_14[8] and x <= angle_litda_14[9]:
		x = 13 + 0.2		
	elif x > angle_litda_14[9] and x <= angle_litda_13[0]:
		x = 13 + 0.1

	#13
	elif x > angle_litda_13[0] and x <= angle_litda_13[1]:
		x = 13
	elif x > angle_litda_13[1] and x <= angle_litda_13[2]:
		x = 12 + 0.9 
	elif x > angle_litda_13[2] and x <= angle_litda_13[3]:
		x = 12 + 0.8 
	elif x > angle_litda_13[3] and x <= angle_litda_13[4]:
		x = 12 + 0.7 
	elif x > angle_litda_13[4] and x <= angle_litda_13[5]:
		x = 12 + 0.6 
	elif x > angle_litda_13[5] and x <= angle_litda_13[6]:
		x = 12 + 0.5 
	elif x > angle_litda_13[6] and x <= angle_litda_13[7]:
		x = 12 + 0.4
	elif x > angle_litda_13[7] and x <= angle_litda_13[8]:
		x = 12 + 0.3
	elif x > angle_litda_13[8] and x <= angle_litda_13[9]:
		x = 12 + 0.2		
	elif x > angle_litda_13[9] and x <= angle_litda_12[0]:
		x = 12 + 0.1

	#12
	elif x > angle_litda_12[0] and x <= angle_litda_12[1]:
		x = 12
	elif x > angle_litda_12[1] and x <= angle_litda_12[2]:
		x = 11 + 0.9 
	elif x > angle_litda_12[2] and x <= angle_litda_12[3]:
		x = 11 + 0.8 
	elif x > angle_litda_12[3] and x <= angle_litda_12[4]:
		x = 11 + 0.7 
	elif x > angle_litda_12[4] and x <= angle_litda_12[5]:
		x = 11 + 0.6 
	elif x > angle_litda_12[5] and x <= angle_litda_12[6]:
		x = 11 + 0.5 
	elif x > angle_litda_12[6] and x <= angle_litda_12[7]:
		x = 11 + 0.4
	elif x > angle_litda_12[7] and x <= angle_litda_12[8]:
		x = 11 + 0.3
	elif x > angle_litda_12[8] and x <= angle_litda_12[9]:
		x = 11 + 0.2		
	elif x > angle_litda_12[9] and x <= angle_litda_11[0]:
		x = 11 + 0.1

	#11
	elif x > angle_litda_11[0] and x <= angle_litda_11[1]:
		x = 11
	elif x > angle_litda_11[1] and x <= angle_litda_11[2]:
		x = 10 + 0.9 
	elif x > angle_litda_11[2] and x <= angle_litda_11[3]:
		x = 10 + 0.8 
	elif x > angle_litda_11[3] and x <= angle_litda_11[4]:
		x = 10 + 0.7 
	elif x > angle_litda_11[4] and x <= angle_litda_11[5]:
		x = 10 + 0.6 
	elif x > angle_litda_11[5] and x <= angle_litda_11[6]:
		x = 10 + 0.5 
	elif x > angle_litda_11[6] and x <= angle_litda_11[7]:
		x = 10 + 0.4
	elif x > angle_litda_11[7] and x <= angle_litda_11[8]:
		x = 10 + 0.3
	elif x > angle_litda_11[8] and x <= angle_litda_11[9]:
		x = 10 + 0.2		
	elif x > angle_litda_11[9] and x <= angle_litda_10[0]:
		x = 10 + 0.1

	#10
	elif x > angle_litda_10[0] and x <= angle_litda_10[1]:
		x = 10
	elif x > angle_litda_10[1] and x <= angle_litda_10[2]:
		x = 9 + 0.9 
	elif x > angle_litda_10[2] and x <= angle_litda_10[3]:
		x = 9 + 0.8 
	elif x > angle_litda_10[3] and x <= angle_litda_10[4]:
		x = 9 + 0.7 
	elif x > angle_litda_10[4] and x <= angle_litda_10[5]:
		x = 9 + 0.6 
	elif x > angle_litda_10[5] and x <= angle_litda_10[6]:
		x = 9 + 0.5 
	elif x > angle_litda_10[6] and x <= angle_litda_10[7]:
		x = 9 + 0.4
	elif x > angle_litda_10[7] and x <= angle_litda_10[8]:
		x = 9 + 0.3
	elif x > angle_litda_10[8] and x <= angle_litda_10[9]:
		x = 9 + 0.2		
	elif x > angle_litda_10[9] and x <= angle_litda_9[0]:
		x = 9 + 0.1

	#9
	elif x > angle_litda_9[0] and x <= angle_litda_9[1]:
		x = 9
	elif x > angle_litda_9[1] and x <= angle_litda_9[2]:
		x = 8 + 0.9 
	elif x > angle_litda_9[2] and x <= angle_litda_9[3]:
		x = 8 + 0.8 
	elif x > angle_litda_9[3] and x <= angle_litda_9[4]:
		x = 8 + 0.7 
	elif x > angle_litda_9[4] and x <= angle_litda_9[5]:
		x = 8 + 0.6 
	elif x > angle_litda_9[5] and x <= angle_litda_9[6]:
		x = 8 + 0.5 
	elif x > angle_litda_9[6] and x <= angle_litda_9[7]:
		x = 8 + 0.4
	elif x > angle_litda_9[7] and x <= angle_litda_9[8]:
		x = 8 + 0.3
	elif x > angle_litda_9[8] and x <= angle_litda_9[9]:
		x = 8 + 0.2		
	elif x > angle_litda_9[9] and x <= angle_litda_8[0]:
		x = 8 + 0.1

	#8
	elif x > angle_litda_8[0] and x <= angle_litda_8[1]:
		x = 8
	elif x > angle_litda_8[1] and x <= angle_litda_8[2]:
		x = 7 + 0.9 
	elif x > angle_litda_8[2] and x <= angle_litda_8[3]:
		x = 7 + 0.8 
	elif x > angle_litda_8[3] and x <= angle_litda_8[4]:
		x = 7 + 0.7 
	elif x > angle_litda_8[4] and x <= angle_litda_8[5]:
		x = 7 + 0.6 
	elif x > angle_litda_8[5] and x <= angle_litda_8[6]:
		x = 7 + 0.5 
	elif x > angle_litda_8[6] and x <= angle_litda_8[7]:
		x = 7 + 0.4
	elif x > angle_litda_8[7] and x <= angle_litda_8[8]:
		x = 7 + 0.3
	elif x > angle_litda_8[8] and x <= angle_litda_8[9]:
		x = 7 + 0.2		
	elif x > angle_litda_8[9] and x <= angle_litda_7[0]:
		x = 7 + 0.1

	#7
	elif x > angle_litda_7[0] and x <= angle_litda_7[1]:
		x = 7
	elif x > angle_litda_7[1] and x <= angle_litda_7[2]:
		x = 6 + 0.9 
	elif x > angle_litda_7[2] and x <= angle_litda_7[3]:
		x = 6 + 0.8 
	elif x > angle_litda_7[3] and x <= angle_litda_7[4]:
		x = 6 + 0.7 
	elif x > angle_litda_7[4] and x <= angle_litda_7[5]:
		x = 6 + 0.6 
	elif x > angle_litda_7[5] and x <= angle_litda_7[6]:
		x = 6 + 0.5 
	elif x > angle_litda_7[6] and x <= angle_litda_7[7]:
		x = 6 + 0.4
	elif x > angle_litda_7[7] and x <= angle_litda_7[8]:
		x = 6 + 0.3
	elif x > angle_litda_7[8] and x <= angle_litda_7[9]:
		x = 6 + 0.2		
	elif x > angle_litda_7[9] and x <= angle_litda_6[0]:
		x = 6 + 0.1

	#6
	elif x > angle_litda_6[0] and x <= angle_litda_6[1]:
		x = 6
	elif x > angle_litda_6[1] and x <= angle_litda_6[2]:
		x = 5 + 0.9 
	elif x > angle_litda_6[2] and x <= angle_litda_6[3]:
		x = 5 + 0.8 
	elif x > angle_litda_6[3] and x <= angle_litda_6[4]:
		x = 5 + 0.7 
	elif x > angle_litda_6[4] and x <= angle_litda_6[5]:
		x = 5 + 0.6 
	elif x > angle_litda_6[5] and x <= angle_litda_6[6]:
		x = 5 + 0.5 
	elif x > angle_litda_6[6] and x <= angle_litda_6[7]:
		x = 5 + 0.4
	elif x > angle_litda_6[7] and x <= angle_litda_6[8]:
		x = 5 + 0.3
	elif x > angle_litda_6[8] and x <= angle_litda_6[9]:
		x = 5 + 0.2		
	elif x > angle_litda_6[9] and x <= angle_litda_5[0]:
		x = 5 + 0.1

	#5
	elif x > angle_litda_5[0] and x <= angle_litda_5[1]:
		x = 5
	elif x > angle_litda_5[1] and x <= angle_litda_5[2]:
		x = 4 + 0.9 
	elif x > angle_litda_5[2] and x <= angle_litda_5[3]:
		x = 4 + 0.8 
	elif x > angle_litda_5[3] and x <= angle_litda_5[4]:
		x = 4 + 0.7 
	elif x > angle_litda_5[4] and x <= angle_litda_5[5]:
		x = 4 + 0.6 
	elif x > angle_litda_5[5] and x <= angle_litda_5[6]:
		x = 4 + 0.5 
	elif x > angle_litda_5[6] and x <= angle_litda_5[7]:
		x = 4 + 0.4
	elif x > angle_litda_5[7] and x <= angle_litda_5[8]:
		x = 4 + 0.3
	elif x > angle_litda_5[8] and x <= angle_litda_5[9]:
		x = 4 + 0.2		
	elif x > angle_litda_5[9] and x <= angle_litda_4[0]:
		x = 4 + 0.1

	#4
	elif x > angle_litda_4[0] and x <= angle_litda_4[1]:
		x = 4
	elif x > angle_litda_4[1] and x <= angle_litda_4[2]:
		x = 3 + 0.9 
	elif x > angle_litda_4[2] and x <= angle_litda_4[3]:
		x = 3 + 0.8 
	elif x > angle_litda_4[3] and x <= angle_litda_4[4]:
		x = 3 + 0.7 
	elif x > angle_litda_4[4] and x <= angle_litda_4[5]:
		x = 3 + 0.6 
	elif x > angle_litda_4[5] and x <= angle_litda_4[6]:
		x = 3 + 0.5 
	elif x > angle_litda_4[6] and x <= angle_litda_4[7]:
		x = 3 + 0.4
	elif x > angle_litda_4[7] and x <= angle_litda_4[8]:
		x = 3 + 0.3
	elif x > angle_litda_4[8] and x <= angle_litda_4[9]:
		x = 3 + 0.2		
	elif x > angle_litda_4[9] and x <= angle_litda_3[0]:
		x = 3 + 0.1

	#3
	elif x > angle_litda_3[0] and x <= angle_litda_3[1]:
		x = 3
	elif x > angle_litda_3[1] and x <= angle_litda_3[2]:
		x = 2 + 0.9 
	elif x > angle_litda_3[2] and x <= angle_litda_3[3]:
		x = 2 + 0.8 
	elif x > angle_litda_3[3] and x <= angle_litda_3[4]:
		x = 2 + 0.7 
	elif x > angle_litda_3[4] and x <= angle_litda_3[5]:
		x = 2 + 0.6 
	elif x > angle_litda_3[5] and x <= angle_litda_3[6]:
		x = 2 + 0.5 
	elif x > angle_litda_3[6] and x <= angle_litda_3[7]:
		x = 2 + 0.4
	elif x > angle_litda_3[7] and x <= angle_litda_3[8]:
		x = 2 + 0.3
	elif x > angle_litda_3[8] and x <= angle_litda_3[9]:
		x = 2 + 0.2		
	elif x > angle_litda_3[9] and x <= angle_litda_2[0]:
		x = 2 + 0.1

	#2
	elif x > angle_litda_2[0] and x <= angle_litda_2[1]:
		x = 2
	elif x > angle_litda_2[1] and x <= angle_litda_2[2]:
		x = 1 + 0.9 
	elif x > angle_litda_2[2] and x <= angle_litda_2[3]:
		x = 1 + 0.8 
	elif x > angle_litda_2[3] and x <= angle_litda_2[4]:
		x = 1 + 0.7 
	elif x > angle_litda_2[4] and x <= angle_litda_2[5]:
		x = 1 + 0.6 
	elif x > angle_litda_2[5] and x <= angle_litda_2[6]:
		x = 1 + 0.5 
	elif x > angle_litda_2[6] and x <= angle_litda_2[7]:
		x = 1 + 0.4
	elif x > angle_litda_2[7] and x <= angle_litda_2[8]:
		x = 1 + 0.3
	elif x > angle_litda_2[8] and x <= angle_litda_2[9]:
		x = 1 + 0.2		
	elif x > angle_litda_2[9] and x <= angle_litda_1[0]:
		x = 1 + 0.1

	#1
	elif x > angle_litda_1[0] and x <= angle_litda_1[1]:
		x = 1
	elif x > angle_litda_1[1] and x <= angle_litda_1[2]:
		x = 0 + 0.9 
	elif x > angle_litda_1[2] and x <= angle_litda_1[3]:
		x = 0 + 0.8 
	elif x > angle_litda_1[3] and x <= angle_litda_1[4]:
		x = 0 + 0.7 
	elif x > angle_litda_1[4] and x <= angle_litda_1[5]:
		x = 0 + 0.6 
	elif x > angle_litda_1[5] and x <= angle_litda_1[6]:
		x = 0 + 0.5 
	elif x > angle_litda_1[6] and x <= angle_litda_1[7]:
		x = 0 + 0.4
	elif x > angle_litda_1[7] and x <= angle_litda_1[8]:
		x = 0 + 0.3
	elif x > angle_litda_1[8] and x <= angle_litda_1[9]:
		x = 0 + 0.2		
	elif x > angle_litda_1[9] and x < 240:
		x = 0 + 0.1


	elif x == 240:
		x = 0 

	#1
	elif x > 240 and x <= angle_litda2_1[1]:
		x = 0 + 0.1 
	elif x > angle_litda2_1[1] and x <= angle_litda2_1[2]:
		x = 0 + 0.2 
	elif x > angle_litda2_1[2] and x <= angle_litda2_1[3]:
		x = 0 + 0.3 
	elif x > angle_litda2_1[3] and x <= angle_litda2_1[4]:
		x = 0 + 0.4 
	elif x > angle_litda2_1[4] and x <= angle_litda2_1[5]:
		x = 0 + 0.5 
	elif x > angle_litda2_1[5] and x <= angle_litda2_1[6]:
		x = 0 + 0.6
	elif x > angle_litda2_1[6] and x <= angle_litda2_1[7]:
		x = 0 + 0.7
	elif x > angle_litda2_1[7] and x <= angle_litda2_1[8]:
		x = 0 + 0.8		
	elif x > angle_litda2_1[8] and x <= angle_litda2_1[9]:
		x = 0 + 0.9
	elif x > angle_litda2_1[9] and x <= angle_litda2_2[0]:
		x = 1

	#2
	elif x > angle_litda2_2[0] and x <= angle_litda2_2[1]:
		x = 1 + 0.1 
	elif x > angle_litda2_2[1] and x <= angle_litda2_2[2]:
		x = 1 + 0.2 
	elif x > angle_litda2_2[2] and x <= angle_litda2_2[3]:
		x = 1 + 0.3 
	elif x > angle_litda2_2[3] and x <= angle_litda2_2[4]:
		x = 1 + 0.4 
	elif x > angle_litda2_2[4] and x <= angle_litda2_2[5]:
		x = 1 + 0.5 
	elif x > angle_litda2_2[5] and x <= angle_litda2_2[6]:
		x = 1 + 0.6
	elif x > angle_litda2_2[6] and x <= angle_litda2_2[7]:
		x = 1 + 0.7
	elif x > angle_litda2_2[7] and x <= angle_litda2_2[8]:
		x = 1 + 0.8		
	elif x > angle_litda2_2[8] and x <= angle_litda2_2[9]:
		x = 1 + 0.9
	elif x > angle_litda2_2[9] and x <= angle_litda2_3[0]:
		x = 2

	#3
	elif x > angle_litda2_3[0] and x <= angle_litda2_3[1]:
		x = 2 + 0.1 
	elif x > angle_litda2_3[1] and x <= angle_litda2_3[2]:
		x = 2 + 0.2 
	elif x > angle_litda2_3[2] and x <= angle_litda2_3[3]:
		x = 2 + 0.3 
	elif x > angle_litda2_3[3] and x <= angle_litda2_3[4]:
		x = 2 + 0.4 
	elif x > angle_litda2_3[4] and x <= angle_litda2_3[5]:
		x = 2 + 0.5 
	elif x > angle_litda2_3[5] and x <= angle_litda2_3[6]:
		x = 2 + 0.6
	elif x > angle_litda2_3[6] and x <= angle_litda2_3[7]:
		x = 2 + 0.7
	elif x > angle_litda2_3[7] and x <= angle_litda2_3[8]:
		x = 2 + 0.8		
	elif x > angle_litda2_3[8] and x <= angle_litda2_3[9]:
		x = 2 + 0.9
	elif x > angle_litda2_3[9] and x <= angle_litda2_4[0]:
		x = 3

	#4
	elif x > angle_litda2_4[0] and x <= angle_litda2_4[1]:
		x = 3 + 0.1 
	elif x > angle_litda2_4[1] and x <= angle_litda2_4[2]:
		x = 3 + 0.2 
	elif x > angle_litda2_4[2] and x <= angle_litda2_4[3]:
		x = 3 + 0.3 
	elif x > angle_litda2_4[3] and x <= angle_litda2_4[4]:
		x = 3 + 0.4 
	elif x > angle_litda2_4[4] and x <= angle_litda2_4[5]:
		x = 3 + 0.5 
	elif x > angle_litda2_4[5] and x <= angle_litda2_4[6]:
		x = 3 + 0.6
	elif x > angle_litda2_4[6] and x <= angle_litda2_4[7]:
		x = 3 + 0.7
	elif x > angle_litda2_4[7] and x <= angle_litda2_4[8]:
		x = 3 + 0.8		
	elif x > angle_litda2_4[8] and x <= angle_litda2_4[9]:
		x = 3 + 0.9
	elif x > angle_litda2_4[9] and x <= angle_litda2_5[0]:
		x = 4

	#5
	elif x > angle_litda2_5[0] and x <= angle_litda2_5[1]:
		x = 4 + 0.1 
	elif x > angle_litda2_5[1] and x <= angle_litda2_5[2]:
		x = 4 + 0.2 
	elif x > angle_litda2_5[2] and x <= angle_litda2_5[3]:
		x = 4 + 0.3 
	elif x > angle_litda2_5[3] and x <= angle_litda2_5[4]:
		x = 4 + 0.4 
	elif x > angle_litda2_5[4] and x <= angle_litda2_5[5]:
		x = 4 + 0.5 
	elif x > angle_litda2_5[5] and x <= angle_litda2_5[6]:
		x = 4 + 0.6
	elif x > angle_litda2_5[6] and x <= angle_litda2_5[7]:
		x = 4 + 0.7
	elif x > angle_litda2_5[7] and x <= angle_litda2_5[8]:
		x = 4 + 0.8		
	elif x > angle_litda2_5[8] and x <= angle_litda2_5[9]:
		x = 4 + 0.9
	elif x > angle_litda2_5[9] and x <= angle_litda2_6[0]:
		x = 5

	#6
	elif x > angle_litda2_6[0] and x <= angle_litda2_6[1]:
		x = 5 + 0.1 
	elif x > angle_litda2_6[1] and x <= angle_litda2_6[2]:
		x = 5 + 0.2 
	elif x > angle_litda2_6[2] and x <= angle_litda2_6[3]:
		x = 5 + 0.3 
	elif x > angle_litda2_6[3] and x <= angle_litda2_6[4]:
		x = 5 + 0.4 
	elif x > angle_litda2_6[4] and x <= angle_litda2_6[5]:
		x = 5 + 0.5 
	elif x > angle_litda2_6[5] and x <= angle_litda2_6[6]:
		x = 5 + 0.6
	elif x > angle_litda2_6[6] and x <= angle_litda2_6[7]:
		x = 5 + 0.7
	elif x > angle_litda2_6[7] and x <= angle_litda2_6[8]:
		x = 5 + 0.8		
	elif x > angle_litda2_6[8] and x <= angle_litda2_6[9]:
		x = 5 + 0.9
	elif x > angle_litda2_6[9] and x <= angle_litda2_7[0]:
		x = 6

	#7
	elif x > angle_litda2_7[0] and x <= angle_litda2_7[1]:
		x = 6 + 0.1 
	elif x > angle_litda2_7[1] and x <= angle_litda2_7[2]:
		x = 6 + 0.2 
	elif x > angle_litda2_7[2] and x <= angle_litda2_7[3]:
		x = 6 + 0.3 
	elif x > angle_litda2_7[3] and x <= angle_litda2_7[4]:
		x = 6 + 0.4 
	elif x > angle_litda2_7[4] and x <= angle_litda2_7[5]:
		x = 6 + 0.5 
	elif x > angle_litda2_7[5] and x <= angle_litda2_7[6]:
		x = 6 + 0.6
	elif x > angle_litda2_7[6] and x <= angle_litda2_7[7]:
		x = 6 + 0.7
	elif x > angle_litda2_7[7] and x <= angle_litda2_7[8]:
		x = 6 + 0.8		
	elif x > angle_litda2_7[8] and x <= angle_litda2_7[9]:
		x = 6 + 0.9
	elif x > angle_litda2_7[9] and x <= angle_litda2_8[0]:
		x = 7

	#8
	elif x > angle_litda2_8[0] and x <= angle_litda2_8[1]:
		x = 7 + 0.1 
	elif x > angle_litda2_8[1] and x <= angle_litda2_8[2]:
		x = 7 + 0.2 
	elif x > angle_litda2_8[2] and x <= angle_litda2_8[3]:
		x = 7 + 0.3 
	elif x > angle_litda2_8[3] and x <= angle_litda2_8[4]:
		x = 7 + 0.4 
	elif x > angle_litda2_8[4] and x <= angle_litda2_8[5]:
		x = 7 + 0.5 
	elif x > angle_litda2_8[5] and x <= angle_litda2_8[6]:
		x = 7 + 0.6
	elif x > angle_litda2_8[6] and x <= angle_litda2_8[7]:
		x = 7 + 0.7
	elif x > angle_litda2_8[7] and x <= angle_litda2_8[8]:
		x = 7 + 0.8		
	elif x > angle_litda2_8[8] and x <= angle_litda2_8[9]:
		x = 7 + 0.9
	elif x > angle_litda2_8[9] and x <= angle_litda2_9[0]:
		x = 8

	#9
	elif x > angle_litda2_9[0] and x <= angle_litda2_9[1]:
		x = 8 + 0.1 
	elif x > angle_litda2_9[1] and x <= angle_litda2_9[2]:
		x = 8 + 0.2 
	elif x > angle_litda2_9[2] and x <= angle_litda2_9[3]:
		x = 8 + 0.3 
	elif x > angle_litda2_9[3] and x <= angle_litda2_9[4]:
		x = 8 + 0.4 
	elif x > angle_litda2_9[4] and x <= angle_litda2_9[5]:
		x = 8 + 0.5 
	elif x > angle_litda2_9[5] and x <= angle_litda2_9[6]:
		x = 8 + 0.6
	elif x > angle_litda2_9[6] and x <= angle_litda2_9[7]:
		x = 8 + 0.7
	elif x > angle_litda2_9[7] and x <= angle_litda2_9[8]:
		x = 8 + 0.8		
	elif x > angle_litda2_9[8] and x <= angle_litda2_9[9]:
		x = 8 + 0.9
	elif x > angle_litda2_9[9] and x <= angle_litda2_10[0]:
		x = 9

	#10
	elif x > angle_litda2_10[0] and x <= angle_litda2_10[1]:
		x = 9 + 0.1 
	elif x > angle_litda2_10[1] and x <= angle_litda2_10[2]:
		x = 9 + 0.2 
	elif x > angle_litda2_10[2] and x <= angle_litda2_10[3]:
		x = 9 + 0.3 
	elif x > angle_litda2_10[3] and x <= angle_litda2_10[4]:
		x = 9 + 0.4 
	elif x > angle_litda2_10[4] and x <= angle_litda2_10[5]:
		x = 9 + 0.5 
	elif x > angle_litda2_10[5] and x <= angle_litda2_10[6]:
		x = 9 + 0.6
	elif x > angle_litda2_10[6] and x <= angle_litda2_10[7]:
		x = 9 + 0.7
	elif x > angle_litda2_10[7] and x <= angle_litda2_10[8]:
		x = 9 + 0.8		
	elif x > angle_litda2_10[8] and x <= angle_litda2_10[9]:
		x = 9 + 0.9
	elif x > angle_litda2_10[9] and x <= angle_litda2_11[0]:
		x = 10

	#11
	elif x > angle_litda2_11[0] and x <= angle_litda2_11[1]:
		x = 10 + 0.1 
	elif x > angle_litda2_11[1] and x <= angle_litda2_11[2]:
		x = 10 + 0.2 
	elif x > angle_litda2_11[2] and x <= angle_litda2_11[3]:
		x = 10 + 0.3 
	elif x > angle_litda2_11[3] and x <= angle_litda2_11[4]:
		x = 10 + 0.4 
	elif x > angle_litda2_11[4] and x <= angle_litda2_11[5]:
		x = 10 + 0.5 
	elif x > angle_litda2_11[5] and x <= angle_litda2_11[6]:
		x = 10 + 0.6
	elif x > angle_litda2_11[6] and x <= angle_litda2_11[7]:
		x = 10 + 0.7
	elif x > angle_litda2_11[7] and x <= angle_litda2_11[8]:
		x = 10 + 0.8		
	elif x > angle_litda2_11[8] and x <= angle_litda2_11[9]:
		x = 10 + 0.9
	elif x > angle_litda2_11[9] and x <= angle_litda2_12[0]:
		x = 11

	#12
	elif x > angle_litda2_12[0] and x <= angle_litda2_12[1]:
		x = 11 + 0.1 
	elif x > angle_litda2_12[1] and x <= angle_litda2_12[2]:
		x = 11 + 0.2 
	elif x > angle_litda2_12[2] and x <= angle_litda2_12[3]:
		x = 11 + 0.3 
	elif x > angle_litda2_12[3] and x <= angle_litda2_12[4]:
		x = 11 + 0.4 
	elif x > angle_litda2_12[4] and x <= angle_litda2_12[5]:
		x = 11 + 0.5 
	elif x > angle_litda2_12[5] and x <= angle_litda2_12[6]:
		x = 11 + 0.6
	elif x > angle_litda2_12[6] and x <= angle_litda2_12[7]:
		x = 11 + 0.7
	elif x > angle_litda2_12[7] and x <= angle_litda2_12[8]:
		x = 11 + 0.8		
	elif x > angle_litda2_12[8] and x <= angle_litda2_12[9]:
		x = 11 + 0.9
	elif x > angle_litda2_12[9] and x <= angle_litda2_13[0]:
		x = 12

	#13
	elif x > angle_litda2_13[0] and x <= angle_litda2_13[1]:
		x = 12 + 0.1 
	elif x > angle_litda2_13[1] and x <= angle_litda2_13[2]:
		x = 12 + 0.2 
	elif x > angle_litda2_13[2] and x <= angle_litda2_13[3]:
		x = 12 + 0.3 
	elif x > angle_litda2_13[3] and x <= angle_litda2_13[4]:
		x = 12 + 0.4 
	elif x > angle_litda2_13[4] and x <= angle_litda2_13[5]:
		x = 12 + 0.5 
	elif x > angle_litda2_13[5] and x <= angle_litda2_13[6]:
		x = 12 + 0.6
	elif x > angle_litda2_13[6] and x <= angle_litda2_13[7]:
		x = 12 + 0.7
	elif x > angle_litda2_13[7] and x <= angle_litda2_13[8]:
		x = 12 + 0.8		
	elif x > angle_litda2_13[8] and x <= angle_litda2_13[9]:
		x = 12 + 0.9
	elif x > angle_litda2_13[9] and x <= angle_litda2_14[0]:
		x = 13

	#14
	elif x > angle_litda2_14[0] and x <= angle_litda2_14[1]:
		x = 13 + 0.1 
	elif x > angle_litda2_14[1] and x <= angle_litda2_14[2]:
		x = 13 + 0.2 
	elif x > angle_litda2_14[2] and x <= angle_litda2_14[3]:
		x = 13 + 0.3 
	elif x > angle_litda2_14[3] and x <= angle_litda2_14[4]:
		x = 13 + 0.4 
	elif x > angle_litda2_14[4] and x <= angle_litda2_14[5]:
		x = 13 + 0.5 
	elif x > angle_litda2_14[5] and x <= angle_litda2_14[6]:
		x = 13 + 0.6
	elif x > angle_litda2_14[6] and x <= angle_litda2_14[7]:
		x = 13 + 0.7
	elif x > angle_litda2_14[7] and x <= angle_litda2_14[8]:
		x = 13 + 0.8		
	elif x > angle_litda2_14[8] and x <= angle_litda2_14[9]:
		x = 13 + 0.9
	elif x > angle_litda2_14[9] and x <= angle_litda2_15[0]:
		x = 14

	#15
	elif x > angle_litda2_15[0] and x <= angle_litda2_15[1]:
		x = 14 + 0.1 
	elif x > angle_litda2_15[1] and x <= angle_litda2_15[2]:
		x = 14 + 0.2 
	elif x > angle_litda2_15[2] and x <= angle_litda2_15[3]:
		x = 14 + 0.3 
	elif x > angle_litda2_15[3] and x <= angle_litda2_15[4]:
		x = 14 + 0.4 
	elif x > angle_litda2_15[4] and x <= angle_litda2_15[5]:
		x = 14 + 0.5 
	elif x > angle_litda2_15[5] and x <= angle_litda2_15[6]:
		x = 14 + 0.6
	elif x > angle_litda2_15[6] and x <= angle_litda2_15[7]:
		x = 14 + 0.7
	elif x > angle_litda2_15[7] and x <= angle_litda2_15[8]:
		x = 14 + 0.8		
	elif x > angle_litda2_15[8] and x <= angle_litda2_15[9]:
		x = 14 + 0.9
	elif x > angle_litda2_15[9] and x <= angle_litda2_16[0]:
		x = 15

	#16
	elif x > angle_litda2_16[0] and x <= angle_litda2_16[1]:
		x = 15 + 0.1 
	elif x > angle_litda2_16[1] and x <= angle_litda2_16[2]:
		x = 15 + 0.2 
	elif x > angle_litda2_16[2] and x <= angle_litda2_16[3]:
		x = 15 + 0.3 
	elif x > angle_litda2_16[3] and x <= angle_litda2_16[4]:
		x = 15 + 0.4 
	elif x > angle_litda2_16[4] and x <= angle_litda2_16[5]:
		x = 15 + 0.5 
	elif x > angle_litda2_16[5] and x <= angle_litda2_16[6]:
		x = 15 + 0.6
	elif x > angle_litda2_16[6] and x <= angle_litda2_16[7]:
		x = 15 + 0.7
	elif x > angle_litda2_16[7] and x <= angle_litda2_16[8]:
		x = 15 + 0.8		
	elif x > angle_litda2_16[8] and x <= angle_litda2_16[9]:
		x = 15 + 0.9
	elif x > angle_litda2_16[9] and x <= angle_litda2_17[0]:
		x = 16

	#17
	elif x > angle_litda2_17[0] and x <= angle_litda2_17[1]:
		x = 16 + 0.1 
	elif x > angle_litda2_17[1] and x <= angle_litda2_17[2]:
		x = 16 + 0.2 
	elif x > angle_litda2_17[2] and x <= angle_litda2_17[3]:
		x = 16 + 0.3 
	elif x > angle_litda2_17[3] and x <= angle_litda2_17[4]:
		x = 16 + 0.4 
	elif x > angle_litda2_17[4] and x <= angle_litda2_17[5]:
		x = 16 + 0.5 
	elif x > angle_litda2_17[5] and x <= angle_litda2_17[6]:
		x = 16 + 0.6
	elif x > angle_litda2_17[6] and x <= angle_litda2_17[7]:
		x = 16 + 0.7
	elif x > angle_litda2_17[7] and x <= angle_litda2_17[8]:
		x = 16 + 0.8		
	elif x > angle_litda2_17[8] and x <= angle_litda2_17[9]:
		x = 16 + 0.9
	elif x > angle_litda2_17[9] and x <= angle_litda2_18[0]:
		x = 17

	#18
	elif x > angle_litda2_18[0] and x <= angle_litda2_18[1]:
		x = 17 + 0.1 
	elif x > angle_litda2_18[1] and x <= angle_litda2_18[2]:
		x = 17 + 0.2 
	elif x > angle_litda2_18[2] and x <= angle_litda2_18[3]:
		x = 17 + 0.3 
	elif x > angle_litda2_18[3] and x <= angle_litda2_18[4]:
		x = 17 + 0.4 
	elif x > angle_litda2_18[4] and x <= angle_litda2_18[5]:
		x = 17 + 0.5 
	elif x > angle_litda2_18[5] and x <= angle_litda2_18[6]:
		x = 17 + 0.6
	elif x > angle_litda2_18[6] and x <= angle_litda2_18[7]:
		x = 17 + 0.7
	elif x > angle_litda2_18[7] and x <= angle_litda2_18[8]:
		x = 17 + 0.8		
	elif x > angle_litda2_18[8] and x <= angle_litda2_18[9]:
		x = 17 + 0.9
	elif x > angle_litda2_18[9] and x <= 480:
		x = 18

	else :
		x = "no detect"

	return x

if __name__ == '__main__':
	print(line_angle(239))
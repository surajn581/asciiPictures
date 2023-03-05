import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageFont, ImageDraw, Image  

Width = 100
Height = 100
cap = cv2.VideoCapture(0)
# cap.set(3, Width)
# cap.set(4, Height)
# cap.set(10, 150)

#densityMap = '''$@@B%8&WMM###HoahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.           '''
# densityMap = '#HXI0O+_1l'
densityMap = 'Ñ@&#eaO|!*+;:=-,._ '
densityMap = np.array( list( densityMap ) )

while True:
	success, img = cap.read()
	img = cv2.flip(img, 1)
	img = cv2.resize(img, (100,100))
	cv2.imshow("input feed", img)

	img = img[:,:,1].astype('float64')
	img *= float(len(densityMap)-1)/img.max() 
	img = img.astype(int)

	im = densityMap[img]

	width = int(1303*(img.shape[1]/100))
	height = int(1500*(img.shape[0]/100))
	newImg = np.full((height, width, 3), 255, dtype = np.uint8)
	font = ImageFont.truetype("consola.ttf", 24)
	pil_im = Image.fromarray(newImg)
	draw = ImageDraw.Draw(pil_im)
	for i,row in enumerate( im ):
		org = (0, 15 * i)
		text = ''.join(row)
		draw.text( org, text, font=font, fill=(0, 0, 0))  
	    
	outImg = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
	outImg = cv2.resize(outImg, (700, 700))
	cv2.imshow("output feed", outImg)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
	

# img = cv2.imread('suraj_negi.jpg', 0)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# img = cv2.resize(img, (50, 50))

# #densityMap = '''$@@B%8&WMM###HoahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'.           '''
# # densityMap = '#HXI0O+_1l'
# densityMap = 'Ñ@&#eaO|!*+;:=-,._ '
# densityMap = np.array( list( densityMap ) )

# cv2.imshow('normal image', img)
# img = img[:,:,1].astype('float64')
# img *= float(len(densityMap)-1)/img.max() 
# img = img.astype(int)

# im = densityMap[img]

# width = int(1303*(img.shape[1]/100))
# height = int(1500*(img.shape[0]/100))
# newImg = np.full((height, width, 3), 255, dtype = np.uint8)
# font = ImageFont.truetype("consola.ttf", 24)
# pil_im = Image.fromarray(newImg)
# draw = ImageDraw.Draw(pil_im)
# for i,row in enumerate( im ):
#     org = (0, 15 * i)
#     text = ''.join(row)    
#     draw.text( org, text, font=font, fill=(0, 0, 0))  
    
# opencvImage = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
# cv2.imshow('ascii image', opencvImage)

# cv2.waitKey(0)
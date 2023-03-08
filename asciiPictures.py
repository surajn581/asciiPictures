import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import ImageFont, ImageDraw, Image  

Width = 100
Height = 100
cap = cv2.VideoCapture(0)

densityMap = '@&##HHIIOO;;::,,... '
densityMap = np.array( list( densityMap ) )

def deStackImage( img ):
    return img[:,:,1].astype('float64')

def normalizeImage( img, max_, inplace = True ):
    if inplace:
        img *= float(max_)/img.max()
        return img.astype(int)
    return ( img * float(max_)/img.max() ).astype(int)

def getasciiArray( img, map_ ):
    return map_[img]

def getBlankImageFromReferenceImage( img, base, scaleby ):
    width = int( 1300 * img.shape[1] * scaleby )
    height = int( 1500 * img.shape[0] * scaleby )
    return Image.fromarray( np.full( ( height, width, 3 ), 255, dtype = np.uint8 ) )

def writeAsciiArrayOnBlankImage( asciiArray, font ):
    img = getBlankImageFromReferenceImage( asciiArray, 255, 0.01 )
    draw = ImageDraw.Draw( img )
    for i,row in enumerate( asciiArray ):
        org = (0, 15 * i)
        text = ''.join( row )
        draw.text( org, text, font=font, fill=(0, 0, 0) )
    return img

def pilToCV2( pilImage ):
    return cv2.cvtColor(np.array(pilImage), cv2.COLOR_RGB2BGR)

while True:
	success, img = cap.read()
	img = cv2.flip(img, 1)
	img = cv2.resize(img, (100,100))
	cv2.imshow("input feed", img)

	img_		= normalizeImage( deStackImage( img ), len( densityMap ) - 1, inplace = False )
	asciiArray  = getasciiArray( img_, densityMap )
	img_        = writeAsciiArrayOnBlankImage( asciiArray, font = ImageFont.truetype("consola.ttf", 24) )
	outImg 		= pilToCV2( img_ )
	outImg 		= cv2.resize(outImg, (700, 700))
	cv2.imshow("output feed", outImg)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
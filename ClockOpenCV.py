import cv2 as cv
import numpy as np
import math
import colors

import datetime

#  Desigining the clock

image = np.zeros((340,340,3), 'uint8')

image[:]=colors.LIGHT_GRAY

hourLines_start_coordinates = np.array([(170,21), (170,320), (20,170), (320,170), (245,40), (300,95), (300,245), (245,300), (95,40), (40,95), (40,245), (95,300)])

hourLines_end_coordinates = np.array([(170,12), (170,329), (11,170), (329,170), (250,32), (308,90), (308,250), (250,308), (90,32), (32,90), (32,250), (90,308)])

for i in range (0,12):
    cv.line(image, tuple(hourLines_start_coordinates[i]), tuple(hourLines_end_coordinates[i]), colors.DARK_GRAY, thickness=1)


cv.circle(image, (170,170) , 159, colors.DARK_GRAY, thickness=2)
cv.circle(image, (170,170) , 5, colors.DARK_GRAY, thickness=-1)
scale = cv.getFontScaleFromHeight(cv.FONT_HERSHEY_SIMPLEX, 10, 0)
dimensions,baseline = cv.getTextSize('Next is Now', cv.FONT_HERSHEY_SIMPLEX, scale, 0)
cv.rectangle(image, (170 - dimensions[0]//2-9, 250 - dimensions[1]//2 - 4), (170 + dimensions[0]//2+9, 250 + dimensions[1]//2 + 5), colors.BLACK, 1)
cv.putText(image, 'Next is Now', (170 - dimensions[0]//2,250+dimensions[1]//2), cv.FONT_HERSHEY_SIMPLEX, scale, colors.DARK_GRAY, thickness= 0)

backup_image = image.copy()

while True:
    time = datetime.datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second
    if hour>12:
        hour-=12
        
    theta_second = (second*6*3.14)/(180)
    theta_minute = (minute*6*3.14)/(180)
    theta_hour = (hour*30*3.14)/(180) + theta_minute/12
    
#     Line for second hand
    if theta_second<=(3.14/2):
        cv.line(image, (170,170), (170 + int(130*math.cos((3.14/2 - theta_second))), 170 - int(130*math.sin((3.14/2 - theta_second)))), colors.DARK_GRAY)
    elif theta_second>(3.14/2) and theta_second<=(3.14):
         cv.line(image, (170,170), (170 + int(130*math.cos((theta_second - 3.14/2))), 170 + int(130*math.sin((theta_second - 3.14/2)))), colors.DARK_GRAY)
    elif theta_second>3.14 and theta_second<=(3*3.14/2):
         cv.line(image, (170,170), (170 - int(130*math.sin((theta_second - 3.14))), 170 + int(130*math.cos((theta_second - 3.14)))), colors.DARK_GRAY)
    elif theta_second>(3*3.14/2) and theta_second<=(2*3.14):
         cv.line(image, (170,170), (170 - int(130*math.cos((theta_second - 3*3.14/2))), 170 - int(130*math.sin((theta_second - 3*3.14/2)))), colors.DARK_GRAY)
    
#    Line for minute hand
    
    if theta_minute <= 3.14/2 :
        cv.line(image, (170,170), (170 + int(97.5*math.cos((3.14/2 - theta_minute))), 170 - int(97.5*math.sin((3.14/2 - theta_minute)))), colors.DARK_GRAY, 1)
    elif theta_minute>(3.14/2) and theta_minute<=3.14:
         cv.line(image, (170,170), (170 + int(97.5*math.cos((theta_minute - 3.14/2))), 170 + int(97.5*math.sin((theta_minute - 3.14/2)))), colors.DARK_GRAY, 1)
    elif theta_minute>3.14 and theta_minute<=(3*3.14/2):
         cv.line(image, (170,170), (170 - int(97.5*math.sin((theta_minute - 3.14))), 170 + int(97.5*math.cos((theta_minute - 3.14)))), colors.DARK_GRAY, 1)
    elif theta_minute>(3*3.14/2) and theta_minute<=(2*3.14):
         cv.line(image, (170,170), (170 - int(97.5*math.cos((theta_minute - 3*3.14/2))), 170 - int(97.5*math.sin((theta_minute - 3*3.14/2)))), colors.DARK_GRAY, 1)
    
#     Line for hour hand
    
    if theta_hour<=(3.14/2):
        cv.line(image, (170,170), (170 + int(65*math.cos((3.14/2 - theta_hour))), 170 - int(65*math.sin((3.14/2 - theta_hour)))), colors.DARK_GRAY, 2)
    elif theta_hour>(3.14/2) and theta_hour<=3.14:
         cv.line(image, (170,170), (170 + int(65*math.cos((theta_hour - 3.14/2))), 170 + int(65*math.sin((theta_hour - 3.14/2)))), colors.DARK_GRAY, 2)
    elif theta_hour>3.14 and theta_hour<=(3*3.14/2):
         cv.line(image, (170,170), (170 - int(65*math.sin((theta_hour - 3.14))), 170 + int(65*math.cos((theta_hour - 3.14)))), colors.DARK_GRAY, 2)
    elif theta_hour>(3*3.14/2) and theta_hour<=(2*3.14):
         cv.line(image, (170,170), (170 - int(65*math.cos((theta_hour - 3*3.14/2))), 170 - int(65*math.sin((theta_hour - 3*3.14/2)))), colors.DARK_GRAY, 2)
    
    cv.imshow('clock', image)

    image = backup_image.copy()
    
    if cv.waitKey(500) & 0xFF == ord('q'):
        break
cv.destroyAllWindows()
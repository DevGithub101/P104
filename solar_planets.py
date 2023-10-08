import cv2
cv2.imread(“solar-system.zip”)
cv2.imshow("output",img)
cv2.waitkey(0)
#Below is the Puttext for all planets with different coordinates.
cv2.putText(img,
            "Sun"
            text,
            (20,220),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.putText(img,
            "Mercury"
            text,
            (30,230),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.putText(img,
            "Venus"
            text,
            (40,240),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})

cv2.putText(img,
            "Earth"
            text,
            (50,250),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.putText(img,
            "Mars"
            text,
            (60,260),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.putText(img,
            "Jupiter"
            text,
            (70,270),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})

cv2.putText(img,
            "Saturn"
            text,
            (80,280),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})

cv2.putText(img,
            "Uranus"
            text,
            (90,290),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.putText(img,
            "Neptune"
            text,
            (100,300),
            fontFace= cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale= 1,
            colour = {0,0,255})
cv2.imwrite(“solar_system.zip”,img)

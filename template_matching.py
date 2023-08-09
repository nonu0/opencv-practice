import numpy as np
import cv2

template1 = cv2.imread('assets/ball.jfif',0)
# template = cv2.imread('assets/ball.png',0)
template = cv2.imread('assets/shoe.png',0)
img1 = cv2.imread('assets/match.jfif',0)
img = cv2.imread('assets/soccer_practice.jpg',0)

img2 = img.copy()
h,w = template.shape

print(template1.shape)
print(img1.shape)
methods = [cv2.TM_CCOEFF,cv2.TM_CCOEFF_NORMED,
           cv2.TM_CCORR,cv2.TM_CCORR_NORMED,
           cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()
    result = cv2.matchTemplate(img2,template,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w,location[1]+h)
    print(bottom_right)
    cv2.rectangle(img2,location,bottom_right,255,5)
    cv2.imshow('match',img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
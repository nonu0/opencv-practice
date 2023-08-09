import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if not cap.isOpened:
    print("Camera not opened")
while True:
    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    # img = cv2.line(frame,(0,0),(width,height),(255,134,89),10)
    # img = cv2.line(img,(0,height),(width,0),(155,134,89),10)
    # img = cv2.rectangle(img,(100,100),(200,200),(155,134,89),-1)
    # img = cv2.circle(img,(100,100),(60),(155,134,89),1)
    # font = cv2.FONT_HERSHEY_COMPLEX
    # img = cv2.putText(img,'CLiff is amazing',(20,height-10),1,font,(0,0,0),5,cv2.LINE_AA)
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    upper = np.array([90,50,51])
    lower = np.array([30,55,85])

    mask = cv2.inRange(hsv,lower,upper)

    result = cv2.bitwise_and(frame,frame,mask=mask)

    image = np.zeros(frame.shape,np.uint8)
    smaller_img = cv2.resize(frame,(0,0),fx=0.5,fy=0.5)

    # image[:height//2,:width//2] = cv2.rotate(smaller_img,cv2.ROTATE_90_COUNTERCLOCKWISE)
    image[height//2:,:width//2] = smaller_img
    image[:height//2,:width//2] = cv2.rotate(smaller_img,cv2.ROTATE_180)
    image[height//2:,width//2:] = smaller_img
    image[:height//2,width//2:] = cv2.rotate(smaller_img,cv2.ROTATE_180)

    cv2.imshow('frame',result)
    cv2.imshow('mask',mask)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()

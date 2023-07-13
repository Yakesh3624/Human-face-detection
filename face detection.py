import cv2

alg = "haarcascade_frontalface_default.xml"

haarcascade = cv2.CascadeClassifier(alg)

cam = cv2.VideoCapture(0)

while True:
    
    img = cam.read()[1]
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    text="0 face detected"
    face = haarcascade.detectMultiScale(grayimg,1.3,9)
    count=0
    for (x,y,w,h) in face:
        count+=1
        cv2.rectangle(img, (x,y) ,(x+w,y+h),(0,250,0),2)
        text = str(count)+" face detected"
    cv2.putText(img,text,(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    cv2.imshow("face",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cam.release()
cv2.destroyAllWindows()

import cv2

cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

while(True):
    ret,frame=cap.read()
    if ret==True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cv2.imshow('Frame',frame)

        out.write(frame)

        if cv2.waitKey(1) & 0XFF == ord('q'):
         break

    else:
        break

cap.realse()
out.realse()
cv2.destroyAllWindows()
import cv2

cap = cv2.VideoCapture('output.avi')

if not cap.isOpened():
    print('Camera open failed')
    exit()


ret, frame = cap.read()
cv2.imshow('frame', frame)
cv2.waitKey(0)
cv2.imwrite('output.jpg', frame)


cap.release()
cv2.destroyAllWindows()
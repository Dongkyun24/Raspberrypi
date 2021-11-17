import cv2

# 카메라 장치 열기
cap = cv2.VideoCapture(0)


if not cap.isOpened():
    print("Camera open failed")
    exit()

# fourcc(four character code)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(frame ,50,100)   

    if not ret:
        break

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    cv2.imshow('edge',edge)
    # 1000 -> 1초, 10 -> 0.01초
    if cv2.waitKey(1) == 27:
        break

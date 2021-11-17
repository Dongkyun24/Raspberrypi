import cv2

img = cv2.imread('Faker.jpg')
img2 = cv2.resize(img, (1280, 720))

gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

cv2.imshow('Faker', img2)
cv2.imshow('Faker', gray)

while True:
    if cv2.waitKey() == 13:
        break

cv2.imwrite('Faker_GRAY.jpg', gray)

cv2.destroyAllWindows()
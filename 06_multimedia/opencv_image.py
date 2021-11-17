import cv2

img = cv2.imread('Faker.jpg')
img = cv2.resize(img, (1280, 720))

cv2.imshow('Faker', img)

edge1 = cv2.Canny(img, 50, 100)
edge2 = cv2.Canny(img, 100, 150)
edge3 = cv2.Canny(img, 150, 200)

cv2.imshow('edge1', edge1)
cv2.imshow('edge2', edge2)
cv2.imshow('edge3', edge3)

cv2.waitKey()

cv2.destroyAllWindows()
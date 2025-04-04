import cv2

# Select an image from your hard drive.
img = cv2. imread('images.jpeg')
if img is None:
    print('Load failed.')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_1 = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

# Experiment with different threshold levels to create a binary copy of the original image.
ret, bw = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find the contours in the image and draw them over the original image.
contours, hierarchy = cv2.findContours(bw, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(img, contours, -1, (0,0,255), 1)

cv2.imshow('contours', img)
cv2.waitKey()
cv2.destroyAllWindows()

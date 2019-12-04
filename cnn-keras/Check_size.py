import cv2

image = cv2.imread("new_image.jpg")
print (image.shape)

# calculate the ratio of the new image to the old image
r = 60.0/ image.shape[1]
dim = (60, int(image.shape[0] * r))

# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.imwrite("new_image.jpg", resized)
cv2.waitKey(0)


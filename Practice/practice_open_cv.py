import cv2

# print(cv2.__version__)

img = cv2.imread("/Users/hieutt/MSE - FPT/Fall 2024/PPR501/Project/In-class/Practice/evn.png")

(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))

# cv2.imshow("Show image", img)
# cv2.waitKey(0)
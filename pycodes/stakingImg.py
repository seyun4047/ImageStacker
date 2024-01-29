import cv2
import numpy as np
import imgResizing

img_path = [f"src/img2/img{i}.JPG" for i in range(1,6,1)]

#  just resize Image
# for i in range(5):
#     imgResizing.resizeImg(img_path[i])

# load the test img
img = [0] * 5
for i in range(5):
    img[i] = cv2.imread(img_path[i])

# cal width, height
imgH, imgW = img[0].shape[:2]

# set space uint16(최대 255*n의 값 수용가능한 uing16 2^16)
reImg = np.zeros((imgH, imgW, 3), dtype=np.uint16)

# cal each pix's avg
for i in range(5):
    reImg += img[i]
reImg = np.array(reImg/5).astype(np.uint8)

# show img
cv2.imshow('reImg', reImg)
cv2.imshow('img1',img[0])
cv2.waitKey(0)
cv2.destroyAllWindows()
# print(reImg)
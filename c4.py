import numpy as np
import cv2


img=cv2.imread('data/messi5.jpg', 0)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('messigray.png', img)

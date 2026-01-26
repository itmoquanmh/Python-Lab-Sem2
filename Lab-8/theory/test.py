import cv2
import numpy as np

def rotate_image(img, angle):
    (h, w) = img.shape[:2]
    (cx, cy) = (w//2, h//2)

    M = cv2.getRotationMatrix2D((cx, cy), angle, 1.0)

    cos = np.abs(M[0, 0])
    sin = np.abs(M[1, 1])

    new_w = int((w*cos) + (h*sin))
    new_h = int((w*sin) + (h*cos))

    M[0, 2] += new_w / 2 -cx
    M[1, 2] += new_h / 2 - cy

    rotated = cv2.warpAffine(img, M, (new_w, new_h))
    return rotated

file = "D:\\ITMO\\first_year\\Python\\Lab-8\\theory\\sample.jpg"
image = cv2.imread(file)
rotated = rotate_image(image, 45)

cv2.imshow("Rotated", rotated)
cv2.waitKey()
cv2.destroyAllWindows()
from PIL import Image
color_image = Image.open("data/home/aistudio/work/images/laoqi.png")
#color_image.show()

gray_image= color_image.convert('L')

import numpy as np 
color_array = np.array(color_image)
print(color_array.shape)

import cv2
img = cv2.imread("data/home/aistudio/work/images/laoqi.png")
cv2.imshow('',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

import matplotlib.pyplot as plt 
plt.imshow(img,cmap='gray')
#plt默认有坐标，消除坐标
plt.xticks([]),plt.yticks([])
plt.show()

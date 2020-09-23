import cv2
import numpy as np
import math

img = cv2.imread('sample1.jpg',1)

'''
cv2.imshow('image',img)

key = cv2.waitKey(0)
if key == 27 :
    cv2.destroyAllWindows()

print(img.shape)
'''
downsize = 15

height = math.floor(img.shape[0]*downsize/100)
width = math.floor(img.shape[1]*downsize/100)

img = cv2.resize(img,(width, height))

'''
cv2.imshow('image',img)

key = cv2.waitKey(0)
if key == 27 :
    cv2.destroyAllWindows()

print(img.shape)


'''

chars = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii = [char for char in chars]

row = []
# average model
for i in range(img.shape[0]):
    col = []
    for j in range(img.shape[1]):
        value = (int(img[i][j][0])+int(img[i][j][1])+int(img[i][j][2]))/3
        unit = 256/65
        index = math.floor(value/unit)
        col.append(ascii[index])
    row.append(col)

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        print(row[i][j],end = "")


    print('')





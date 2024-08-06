import cv2 

img = cv2.imread(“WC25_LLEDGE2.tif”,0) 
# the slash is folder name, and the name after the thing is 
# the number at the end here changes whether or not you have color. 1 is color; 0 is no color
cv2.imshow(“pic”,img)

print(img.shape)

cv2.waitKey(0)
cv2.destroyAllWindows() 

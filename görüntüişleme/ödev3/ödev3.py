import cv2

img = cv2.imread("foti.jpeg")
img = cv2.resize(img, (700, 500))
cevir = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
ret, threshold = cv2.threshold(cevir, 55, 250, cv2.THRESHBINARY)
pirincsay,  = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
print("Pirinc sayisi: ",len(pirincsay))
arkasi = cv2.bitwise_and(img, img, mask=threshold)
cv2.imshow("durum1", img)
cv2.imshow("durum2", arkasi)
cv2.waitKey(0)
cv2.destroyAllWindows()
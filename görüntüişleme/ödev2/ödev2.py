import cv2
import numpy as np
kayit = cv2.VideoCapture(0)
kayit.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
kayit.set(cv2.CAP_PROP_FRAME_HEIGHT, 800)

while True:
    bc, cevir = kayit.read()
    hsv = cv2.cvtColor(cevir, cv2.COLOR_BGR2HSV)
    renk_alt_sinir = np.array([0, 0, 0])
    renk_ust_sinir = np.array([5, 255, 255])
    mask = cv2.inRange(hsv, renk_alt_sinir,renk_ust_sinir)
    red_cevir = cv2.bitwise_and(cevir, cevir, mask=mask)
    cv2.imshow("kapatmak icinn 'q'", cevir)
    cv2.imshow("kapatmak icin 'q'", red_cevir)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
kayit.release()
cv2.destroyAllWindows()
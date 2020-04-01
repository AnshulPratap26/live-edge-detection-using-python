import cv2
def switch(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    smoothen = cv2.GaussianBlur(gray,(5,5),0)
    edge_detect = cv2.Canny(smoothen,30,70)
    ret, thresh = cv2.threshold(edge_detect,70,255,cv2.THRESH_BINARY)
    return thresh

capture = cv2.VideoCapture(0)

while True:
    ret,frame = capture.read()
    cv2.imshow("live edge detection", switch(frame))

    if cv2.waitKey(1) & 0XFF == 27:
        break

capture.release()
cv2.destroyAllWindows()
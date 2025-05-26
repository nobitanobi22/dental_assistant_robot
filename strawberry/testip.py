import cv2

# Replace with your DroidCam IP address
url = "http://10.12.6.233:4747/"

cap = cv2.VideoCapture(url)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("DroidCam Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

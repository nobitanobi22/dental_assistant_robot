import cv2

def test_cameras(max_index=5):
    for i in range(max_index):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            print(f"✅ Camera index {i} is available.")
            ret, frame = cap.read()
            if ret:
                cv2.imshow(f"Camera {i}", frame)
                print("Press any key to close the preview...")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
            cap.release()
        else:
            print(f"❌ Camera index {i} not available.")

test_cameras()

import cv2
import numpy as np
from ultralytics import YOLO

# Load your trained segmentation model
model = YOLO("C:/Users/Sanjeet Kumar/runs/segment/train3/weights/best.pt")

# Path to your saved video
video_path = r"C:\Users\Sanjeet Kumar\Desktop\WhatsApp Video 2025-04-11 at 3.20.34 PM.mp4"
cap = cv2.VideoCapture(video_path)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Get frame shape
    orig_h, orig_w = frame.shape[:2]

    # Run inference
    results = model.predict(source=frame, save=False, show=False, conf=0.25)

    # Copy for overlay
    frame_with_seg = frame.copy()

    for r in results:
        if r.masks is not None:
            masks = r.masks.data.cpu().numpy()
            for mask in masks:
                # Resize mask to match original frame
                mask_resized = cv2.resize(mask, (orig_w, orig_h), interpolation=cv2.INTER_NEAREST)
                colored_mask = (mask_resized * 255).astype('uint8')
                contours, _ = cv2.findContours(colored_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                for cnt in contours:
                    cv2.drawContours(frame_with_seg, [cnt], -1, (0, 255, 0), 2)

    # Show both frames
    cv2.imshow("Original Video Frame", frame)
    cv2.imshow("Segmentation Overlay", frame_with_seg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
from ultralytics import YOLO

model = YOLO("best.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access the webcam.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break
    results = model.predict(frame, verbose=False)

    annotated_frame = results[0].plot()

    cv2.imshow("Webcam Room Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):    # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()

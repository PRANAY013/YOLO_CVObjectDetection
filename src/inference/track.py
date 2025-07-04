import cv2
from ultralytics import YOLO

def main():
    model = YOLO('models/yolov8_custom/weights/best.pt')
    cap = cv2.VideoCapture('data/videotest5.mp4')  

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        # Track objects with persistent IDs
        results = model.track(frame, persist=True, tracker='bytetrack.yaml', max_det=300)
        annotated_frame = results[0].plot()
        cv2.imshow('YOLOv8 Traffic Tracking', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

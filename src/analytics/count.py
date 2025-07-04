import cv2
from ultralytics import YOLO

def main():
    model = YOLO('models/yolov8_custom/weights/best.pt')
    cap = cv2.VideoCapture(0)
    total_counts = {}

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = model(frame)
        boxes = results[0].boxes
        frame_counts = {}
        for box in boxes:
            cls = int(box.cls[0])
            frame_counts[cls] = frame_counts.get(cls, 0) + 1
        for cls, count in frame_counts.items():
            total_counts[cls] = total_counts.get(cls, 0) + count
        annotated_frame = results[0].plot()
        cv2.imshow('YOLOv8 Traffic Counting', annotated_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("Total counts by class:", total_counts)
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

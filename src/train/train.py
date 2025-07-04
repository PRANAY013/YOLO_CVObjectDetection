from ultralytics import YOLO

def train_yolov8():
    model = YOLO('yolov8n.pt')  # Starting with small for speed; can switch to yolov8m/l/x as needed
    model.train(
        data='configs/coco.yaml',
        epochs=3,
        imgsz=320,
        batch=2,
        device='cpu',
        project='models',
        name='yolov8_custom',
        workers=2,
        optimizer='auto',
        verbose=True
    )

if __name__ == "__main__":
    train_yolov8()

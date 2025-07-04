# YOLOv8-Powered Real-Time Multi-Class Traffic Detection System

## 🚦 Project Overview

This project demonstrates a **real-time, multi-class traffic detection and tracking system** built using YOLOv8, PyTorch, and OpenCV.  
The goal was to detect and track vehicles, pedestrians, and other traffic objects in video streams, leveraging the COCO dataset and state-of-the-art deep learning techniques.

## 🛠️ Technologies & Tools Used

- **Python 3.9**
- **PyTorch** (for deep learning/model training)
- **Ultralytics YOLOv8** (object detection and tracking)
- **OpenCV** (video/image processing)
- **COCO Dataset** (for training and evaluation)
- **JSON2YOLO** (COCO to YOLO label conversion)
- **Docker** (for reproducible environments)
- **Jupyter/VS Code** (for prototyping and development)

## 🧩 Project Workflow

1. **Data Preparation**
   - Downloaded COCO images and annotations.
   - Converted COCO JSON annotations to YOLO format using JSON2YOLO.
   - Organized images and labels in a structure compatible with YOLOv8.

2. **Model Training**
   - Used YOLOv8 pre-trained weights (`yolov8n.pt`, `yolov8s.pt`) as a starting point.
   - Fine-tuned on the COCO dataset for relevant classes (cars, people, etc.).
   - Experimented with different model sizes and hyperparameters for speed vs. accuracy.

3. **Detection & Inference**
   - Built a detection pipeline to process video files and display real-time results.
   - Visualized detections with bounding boxes and class labels.

4. **Object Tracking**
   - Integrated YOLOv8’s tracking API (ByteTrack/BoT-SORT) to assign unique IDs and follow objects across frames.
   - Enabled real-time multi-object tracking in video streams.

5. **Analytics & Visualization**
   - Generated training curves, loss/metric graphs, and batch visualizations.
   - Explored object counting and density estimation as potential extensions.

## 📂 Project Structure

```
YOLO_CVObjectDetection/
├── configs/          # Model and dataset YAML configs
├── data/             # Raw images and labels (local only, not in repo)
├── models/           # Trained model weights (local only)
├── src/
│   ├── data/         # Data prep and augmentation scripts
│   ├── train/        # Training scripts
│   ├── inference/    # Detection and tracking scripts
│   ├── analytics/    # Analytics and visualization scripts
│   └── utils.py      # Utilities
├── requirements.txt  # Python dependencies
└── README.md         # Project overview (this file)
```

## 📈 Progress & Improvements

- **Initial Setup:** Established modular codebase and directory structure.
- **Data Pipeline:** Automated conversion and organization of COCO data for YOLOv8.
- **Model Training:** Achieved improving mAP and loss over epochs, validated with visualizations.
- **Detection:** Real-time detection on video, robust to different traffic scenarios.
- **Tracking:** Added persistent object IDs for analytics and traffic flow analysis.

## 🚀 Results

- **Detection:** Model accurately detects cars, people, and other traffic objects in diverse scenes.
- **Tracking:** Successfully assigns and maintains unique IDs for multiple objects in crowded videos.
- **Performance:** Achieved real-time inference speeds on CPU with YOLOv8n/s; higher FPS possible on GPU.
- **Scalability:** Codebase is ready for edge or cloud deployment.

## 🧠 Challenges & Lessons Learned

- **Data conversion** from COCO to YOLO format required careful mapping of class indices.
- **Model limitations** in crowded scenes highlighted the need for advanced architectures or custom fine-tuning.
- **Experimentation** with model sizes and hyperparameters was key to balancing speed and accuracy.

## 📝 Next Steps & Potential Improvements

- **Fine-tune on custom traffic footage** for even higher accuracy in specific environments.
- **Experiment with enhanced YOLOv8 variants** (e.g., SOD-YOLOv8) for better small-object detection.
- **Integrate advanced analytics** (object counting, speed estimation, heatmaps).
- **Deploy on edge devices** (Jetson Nano, Raspberry Pi) or in the cloud.

## 📚 References

- [Ultralytics YOLOv8 Docs](https://docs.ultralytics.com/)
- [COCO Dataset](https://cocodataset.org/)
- [JSON2YOLO](https://github.com/ultralytics/JSON2YOLO)

## 👤 Author

*Pranay*  
*YOLOv8 Traffic Detection Project*  
*July 2025*
# Indoor Object Detection using YOLOv8

This repository implements a real-time indoor object detection system using **YOLOv8** and **OpenCV**. The model detects various household objects from a webcam feed and draws bounding boxes with class labels.

---

## Requirements

Install the required Python packages using pip:

```bash
pip install ultralytics opencv-python numpy
```
Installing Pytorch with cuda is recommended in case of a GPU for better speed.

## Dataset Link
https://www.kaggle.com/datasets/thepbordin/indoor-object-detection

## How to Run
1. Place the trained YOLOv8 model (best.pt) in the root directory.
2. Run the real-time detection script:
```bash
python main.py
```
The webcam will open showing detected indoor objects.

Press q to quit the stream.

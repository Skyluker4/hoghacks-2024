#!/usr/bin/env python3
from ultralytics import YOLO

# Configure the tracking parameters and run the tracker
model = YOLO('yolov8n.pt')
results = model.track(source="./Videos/001-Endzone.mp4", conf=0.01, iou=0.5, show=True)

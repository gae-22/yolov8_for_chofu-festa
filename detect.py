from ultralytics import YOLO


# model = YOLO("yolov8s.pt")  # 物体検知
# model = YOLO("yolov8s-seg.pt")  # セグメンテーション
model = YOLO("yolov8s-pose.pt")  # 姿勢推定

results = model(0, show=True)

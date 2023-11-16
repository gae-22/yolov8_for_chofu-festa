from ultralytics import YOLO


# model = YOLO("yolov8m.pt")  # 物体検知
# model = YOLO("yolov8m-seg.pt")  # セグメンテーション
model = YOLO("yolov8m-pose.pt")  # 姿勢推定

results = model(0, show=True)

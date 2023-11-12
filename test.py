from ultralytics import YOLO

# model = YOLO("yolov8n.pt")
# model = YOLO("yolov8s.pt")
# model = YOLO("yolov8m.pt")
# model = YOLO("yolov8l.pt")
# model = YOLO("yolov8x.pt")

model = YOLO("yolov8n-seg.pt")
# model = YOLO("yolov8s-seg.pt")
# model = YOLO("yolov8m-seg.pt")
# model = YOLO("yolov8l-seg.pt")
# model = YOLO("yolov8x-seg.pt")

results = model(0, show=True)

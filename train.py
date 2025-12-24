from ultralytics import YOLO

model = YOLO("yolov8n.pt")  # pretrained

model.train(
    data="dataset/traffic_sign.yaml",
    epochs=50,
    imgsz=640,
    batch=16,
    name="yolo_vn_traffic_sign"
)

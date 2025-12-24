from ultralytics import YOLO
import cv2

# ===== LOAD MODEL =====
model = YOLO("yolov8n.pt")  # model pretrained (demo)

# ===== LOAD CLASS NAMES (TIẾNG VIỆT) =====
with open("classes_vie.txt", "r", encoding="utf-8") as f:
    class_names = [line.strip() for line in f]

# ===== LOAD VIDEO =====
video_path = "video/test.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Không mở được video:", video_path)
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.4)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            label = f"{class_names[cls_id]} ({conf:.2f})"

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(
                frame,
                label,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

    cv2.imshow("Vietnamese Traffic Sign Detection", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC để thoát
        break

cap.release()
cv2.destroyAllWindows()

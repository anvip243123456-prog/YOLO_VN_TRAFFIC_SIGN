YOLOv8-based Vietnamese Traffic Sign Detection

Nhận dạng Biển báo Giao thông Việt Nam bằng YOLOv8

1\. Introduction | Giới thiệu

🇬🇧 English

Traffic sign detection plays a crucial role in intelligent transportation systems and autonomous driving.

This project focuses on detecting Vietnamese traffic signs using the YOLOv8 object detection model, aiming to achieve high accuracy and real-time performance on both images and videos.

The project is developed as part of an academic thesis, with systematic dataset preparation, training, evaluation, and deployment pipelines.

🇻🇳 Tiếng Việt

Nhận dạng biển báo giao thông là một thành phần quan trọng trong các hệ thống giao thông thông minh và xe tự hành.

Đề tài này tập trung vào việc phát hiện biển báo giao thông Việt Nam bằng mô hình YOLOv8, hướng đến độ chính xác cao và khả năng xử lý thời gian thực trên cả ảnh và video.

Dự án được xây dựng theo hướng nghiên cứu – luận văn, với quy trình chuẩn hóa từ xử lý dữ liệu, huấn luyện, đánh giá đến triển khai mô hình.



2\. Model Overview | Tổng quan mô hình

🇬🇧

Model: YOLOv8 (Ultralytics)

Architecture: One-stage object detector

Strengths:

Real-time detection

High accuracy on video streams

Robust to lighting and motion variations



🇻🇳

Mô hình: YOLOv8 (Ultralytics)

Kiến trúc: Bộ phát hiện đối tượng một giai đoạn (one-stage detector)

Ưu điểm:

Xử lý thời gian thực

Độ chính xác cao trên video

Ổn định trong điều kiện ánh sáng và chuyển động khác nhau



3\. Dataset | Dữ liệu

🇬🇧

Dataset: Vietnamese Traffic Signs

Source: Kaggle

Annotations: YOLO format (.txt)

Classes: Vietnamese traffic sign categories

Due to storage limitations, images and labels are not included in this repository and are ignored via .gitignore.



🇻🇳

Bộ dữ liệu: Vietnamese Traffic Signs

Nguồn: Kaggle

Định dạng nhãn: YOLO (.txt)

Số lớp: Các loại biển báo giao thông Việt Nam

Do dung lượng lớn, ảnh và nhãn không được đưa lên GitHub và đã được loại trừ bằng .gitignore.



4\. Project Structure | Cấu trúc thư mục

YOLO\_VN\_TRAFFIC\_SIGN/

├── .gitignore                 # Ignore dataset, runs, weights

├── README.md                  # Project documentation

├── classes\_vie.txt            # Vietnamese class names

├── dataset/

│   └── traffic\_sign.yaml      # YOLO dataset configuration

├── prepare\_dataset.py         # Dataset preprocessing script

├── gen\_yaml.py                # YAML generation script

├── train.py                   # YOLOv8 training script

└── detect\_video.py            # Video inference script



5\. Installation | Cài đặt

🇬🇧

pip install ultralytics opencv-python torch numpy



🇻🇳

Cài đặt các thư viện cần thiết:

pip install ultralytics opencv-python torch numpy



6\. Training | Huấn luyện mô hình

🇬🇧

python train.py

The training process uses the configuration defined in traffic\_sign.yaml and YOLOv8 pretrained weights.



🇻🇳

Huấn luyện mô hình bằng lệnh:

python train.py

Quá trình huấn luyện sử dụng file cấu hình traffic\_sign.yaml và trọng số pretrained của YOLOv8.



7\. Inference on Video | Nhận dạng trên video

🇬🇧

python detect\_video.py

The model performs real-time detection and outputs bounding boxes with class labels.



🇻🇳

Chạy nhận dạng trên video:

python detect\_video.py

Mô hình sẽ phát hiện biển báo theo thời gian thực và hiển thị nhãn tương ứng.



8\. Experimental Results | Kết quả thực nghiệm

🇬🇧

High detection accuracy on static images

Near real-time performance on video streams

YOLOv8 shows strong robustness compared to traditional detectors



🇻🇳

Độ chính xác cao trên ảnh tĩnh

Hiệu suất gần thời gian thực trên video

YOLOv8 thể hiện tính ổn định vượt trội so với các phương pháp truyền thống



9\. Academic Use | Ứng dụng học thuật

🇬🇧



This repository is designed for:

Bachelor / Engineering thesis

Computer vision research

Intelligent transportation systems



🇻🇳

Repo này phù hợp cho:

Luận văn tốt nghiệp

Nghiên cứu thị giác máy tính

Hệ thống giao thông thông minh



10\. Future Work | Hướng phát triển

🇬🇧

Compare YOLOv8 with SSD and Faster R-CNN

Improve small object detection

Deploy on embedded devices (Jetson, Raspberry Pi)



🇻🇳

So sánh YOLOv8 với SSD và Faster R-CNN

Cải thiện khả năng phát hiện biển nhỏ

Triển khai trên thiết bị nhúng (Jetson, Raspberry Pi)



Author | Tác giả



Le Nguyen Hai An
HUYNH VU MINH HIEU

Faculty of Information Technology

Ton Duc Thang University

Vietnam 🇻🇳




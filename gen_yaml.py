import yaml
import os

# ====== ĐƯỜNG DẪN ======
classes_file = "classes_vie.txt"
yaml_output = "dataset/traffic_sign.yaml"

# ====== ĐỌC DANH SÁCH LỚP ======
with open(classes_file, "r", encoding="utf-8") as f:
    class_names = [line.strip() for line in f if line.strip()]

# ====== TẠO NỘI DUNG YAML ======
data_yaml = {
    "train": "dataset/images/train",
    "val": "dataset/images/val",
    "nc": len(class_names),
    "names": class_names
}

# ====== GHI FILE YAML ======
os.makedirs("dataset", exist_ok=True)

with open(yaml_output, "w", encoding="utf-8") as f:
    yaml.dump(
        data_yaml,
        f,
        allow_unicode=True,
        sort_keys=False
    )

print("Đã tạo traffic_sign.yaml")
print("Số lớp (nc):", len(class_names))
print("File nằm tại:", yaml_output)

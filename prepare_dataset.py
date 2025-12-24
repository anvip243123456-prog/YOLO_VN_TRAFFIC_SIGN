# -*- coding: utf-8 -*-
import os
import shutil
import random
import yaml

# ====== CẤU HÌNH ======
RAW_DATASET = "raw_dataset"  # chứa images/, labels/
OUTPUT_DATASET = "dataset"
TRAIN_RATIO = 0.8
IMAGE_EXT = ".jpg"

# ====== TẠO THƯ MỤC ======
for p in [
    "images/train", "images/val",
    "labels/train", "labels/val"
]:
    os.makedirs(os.path.join(OUTPUT_DATASET, p), exist_ok=True)

# ====== LẤY DANH SÁCH ẢNH ======
images = [f for f in os.listdir(os.path.join(RAW_DATASET, "images")) if f.endswith(IMAGE_EXT)]
random.shuffle(images)

split_idx = int(len(images) * TRAIN_RATIO)
train_files = images[:split_idx]
val_files = images[split_idx:]

def copy_files(file_list, split):
    for f in file_list:
        shutil.copy(
            os.path.join(RAW_DATASET, "images", f),
            os.path.join(OUTPUT_DATASET, "images", split)
        )
        shutil.copy(
            os.path.join(RAW_DATASET, "labels", f.replace(IMAGE_EXT, ".txt")),
            os.path.join(OUTPUT_DATASET, "labels", split)
        )

copy_files(train_files, "train")
copy_files(val_files, "val")

print(f"✅ Train: {len(train_files)} | Val: {len(val_files)}")

# ====== TẠO YAML ======
with open("classes_vie.txt", encoding="utf-8") as f:
    names = f.read().splitlines()

data_yaml = {
    "train": "dataset/images/train",
    "val": "dataset/images/val",
    "nc": len(names),
    "names": names
}

with open("dataset/traffic_sign.yaml", "w", encoding="utf-8") as f:
    yaml.dump(data_yaml, f, allow_unicode=True)

print("✅ Đã tạo dataset/traffic_sign.yaml")

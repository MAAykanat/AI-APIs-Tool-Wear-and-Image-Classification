import os
import shutil
from pathlib import Path
import random

# Parametreler
data_dir = "dataset/flower_photos"  # Veri seti klasörü
train_dir = "dataset/train_flower"  # Eğitim verisi klasörü
test_dir = "dataset/test_flower"    # Test verisi klasörü
test_split = 0.2            # Test verisi oranı (yüzde 20)

# Klasörlerinizi oluşturun (varsa silip yeniden oluşturulacak)
if os.path.exists(train_dir):
    shutil.rmtree(train_dir)
if os.path.exists(test_dir):
    shutil.rmtree(test_dir)

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# Veri seti klasöründe işlem yapma
data_dir = Path(data_dir)

for class_name in os.listdir(data_dir):
    class_path = data_dir / class_name
    if not class_path.is_dir():
        continue  # Eğer alt klasör değilse, geç

    # Resimleri listeleyin ve karıştırın
    images = list(class_path.iterdir())
    images = [img for img in images if img.is_file()]
    random.shuffle(images)  # Resimleri karıştır

    # Eğitim ve test verilerini ayır
    split_index = int(len(images) * (1 - test_split))
    train_images = images[:split_index]
    test_images = images[split_index:]

    # Klasörleri oluşturun ve resimleri kopyalayın
    train_class_dir = Path(train_dir) / class_name
    test_class_dir = Path(test_dir) / class_name
    train_class_dir.mkdir(parents=True, exist_ok=True)
    test_class_dir.mkdir(parents=True, exist_ok=True)

    # Eğitim ve test verilerine resimleri kopyalayın
    for img in train_images:
        shutil.copy(img, train_class_dir / img.name)
    for img in test_images:
        shutil.copy(img, test_class_dir / img.name)

    print(f"Class '{class_name}' processed: {len(train_images)} train, {len(test_images)} test")

print("Veri seti başarıyla ayrıldı.")

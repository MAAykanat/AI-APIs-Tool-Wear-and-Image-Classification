import os
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator  # type: ignore
from tensorflow.keras import layers, models # type: ignore
from tensorflow.keras.applications import EfficientNetB0 # type: ignore
from tensorflow.keras.optimizers import Adam # type: ignore

# Parametreler
train_dir = 'dataset/train_flower'  # Eğitim verisi klasörü
test_dir = 'dataset/test_flower'    # Test verisi klasörü
img_size = (224, 224)       # Resim boyutu (ResNet50 için 224x224 yaygın)
batch_size = 32             # Batch size
epochs = 10                 # Eğitim süresi

# Veri yükleme
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,        # Piksel değerlerini normalize et
    shear_range=0.2,          # Resim üzerinde yatay/veya dikey kaydırma
    zoom_range=0.2,           # Resimde zoom yapma
    horizontal_flip=True)     # Yatay çevirme

test_datagen = ImageDataGenerator(rescale=1.0/255.0)  # Test için sadece normalizasyon

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=img_size,  # Resimleri 224x224'e ölçekle
    batch_size=batch_size,
    class_mode='categorical')  # Kategorik sınıflandırma

test_generator = test_datagen.flow_from_directory(
    test_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical')

# EfficientNetB0 Modeli
base_model = EfficientNetB0(weights='imagenet', include_top=False, input_shape=(img_size[0], img_size[1], 3))
base_model.trainable = False  # Önceden eğitilmiş ağı sabitle (fine-tuning yapmayacağız)

# Modeli oluşturma
model = models.Sequential([
    base_model,
    layers.GlobalAveragePooling2D(),  # Global average pooling
    layers.Dense(1024, activation='relu'),  # Tam bağlantılı katman
    layers.Dropout(0.5),  # Overfitting'i engellemek için dropout
    layers.Dense(train_generator.num_classes, activation='softmax')  # Çıktı katmanı
])

# Modeli derleme
model.compile(optimizer=Adam(), loss='categorical_crossentropy', metrics=['accuracy'])

# Modeli eğitme
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=epochs,
    validation_data=test_generator,
    validation_steps=test_generator.samples // batch_size
)

# Modeli kaydetme
model.save('saved_models/flower_efficientnet_model.h5')
print("Model başarıyla kaydedildi.")
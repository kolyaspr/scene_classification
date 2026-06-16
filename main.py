from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
from PIL import Image
import io
import tensorflow as tf

# === Загрузка модели ===
model = tf.keras.models.load_model("model.h5")

# === Классы ===
CLASS_NAMES = ['buildings', 'forest', 'glacier', 'mountain', 'sea', 'street']

app = FastAPI()

# === Разрешаем запросы со Streamlit ===
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Предобработка изображения ===
def preprocess_image(image: Image.Image):
    image = image.resize((64, 64))
    image = np.array(image) / 255.0  # нормализация
    image = np.expand_dims(image, axis=0)
    return image


# === Endpoint ===
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents)).convert("RGB")

    processed = preprocess_image(image)

    predictions = model.predict(processed)[0]

    predicted_class = CLASS_NAMES[np.argmax(predictions)]

    return {
        "predicted_class": predicted_class,
        "probabilities": {
            CLASS_NAMES[i]: float(predictions[i]) for i in range(len(CLASS_NAMES))
        }
    }
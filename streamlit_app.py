import streamlit as st
import requests
from PIL import Image
import matplotlib.pyplot as plt

# API_URL = "http://127.0.0.1:8000/predict" // Для локального запуска
API_URL = "https://scene-classification-bcyp.onrender.com/predict"

st.title("Классификация ландшафтов")

st.write("Загрузите изображение для классификации")

uploaded_file = st.file_uploader("Выберите изображение", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    # показываем ОРИГИНАЛ
    st.image(image, caption="Загруженное изображение", width=300)

    if st.button("Классифицировать"):
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(API_URL, files=files)

        if response.status_code == 200:
            result = response.json()

            st.subheader("Результат:")
            st.write(f"Предсказанный класс: **{result['predicted_class']}**")

            # === вероятности ===
            probs = result["probabilities"]

            st.subheader("Вероятности:")

            fig, ax = plt.subplots()
            ax.bar(probs.keys(), probs.values())
            ax.set_xticklabels(probs.keys(), rotation=45)

            st.pyplot(fig)

        else:
            st.error("Ошибка при запросе к API")

# Классификатор ландшафтов

## Описание проекта
Веб-приложение для классификации изображений ландшафтов с использованием методов глубокого обучения.

Пользователь загружает изображение, после чего:
1. Выполняется предобработка изображения
2. Изображение отправляется на API
3. Модель выполняет классификацию
4. Возвращается результат и вероятности по классам

Приложение отображает:
- загруженное изображение
- предсказанный класс
- распределение вероятностей по всем классам

Используемые технологии:
- FastAPI — backend (API)
- Streamlit — frontend (интерфейс)
- TensorFlow — нейронные сети
- Matplotlib — визуализация

---

## Датасет

В проекте используется датасет:
**Intel Image Classification**

Ссылка:  
https://www.kaggle.com/datasets/puneet6060/intel-image-classification

Датасет содержит изображения природных сцен, разделённых на 6 классов:
- buildings
- forest
- glacier
- mountain
- sea
- street
---

## Используемые модели

В рамках работы были обучены и сравнены следующие модели:

## 1. Dense (полносвязная сеть)
Простая нейронная сеть, использующая только полносвязные слои.

## 2. VGG-подобная модель
Свёрточная нейронная сеть, основанная на архитектуре VGG.

## 3. Norm + Batch
Модель с использованием:
- Batch Normalization
- нормализации входных данных

## 4. MobileNetV2
Модель на основе предобученной архитектуры MobileNetV2.

Преимущества:
- высокая точность
- быстрая сходимость
- меньшее количество параметров

---

## Сравнение моделей

<img width="569" height="83" alt="image" src="https://github.com/user-attachments/assets/adfbf4ec-4bb6-4d2e-9098-337d71a65d0c" />


---

## Визуализация результатов

<img width="844" height="525" alt="image" src="https://github.com/user-attachments/assets/66b3764a-431b-4c47-8440-63dbb4c879e8" />
<img width="698" height="440" alt="image" src="https://github.com/user-attachments/assets/e1e4fb2a-225f-4a38-a353-c9fc39fcd473" />

---

## Архитектура приложения

Приложение состоит из двух частей:

- Backend (FastAPI) — обработка изображений и работа с моделью
- Frontend (Streamlit) — пользовательский интерфейс

---

## Структура проекта

- `main.py` — FastAPI-бэкенд (загрузка модели и обработка запросов)
- `streamlit_app.py` — Streamlit-фронтенд
- `model.h5` — обученная модель нейронной сети
- `requirements.txt` — зависимости проекта
- `.gitignore` — исключение ненужных файлов (venv/, __pycache__)

---

## Установка и запуск

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/MrQwait/scene_classification
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите FastAPI-бэкенд (в одном терминале):
   ```bash
   uvicorn main:app --reload
   ```

5. Запустите Streamlit-фронтенд (в другом терминале):
   ```bash
   streamlit run app.py
   ```

6. Откройте в браузере: http://127.0.0.1:8000/

## API

https://scene-classification-bcyp.onrender.com/docs

## Streamlit-приложение

https://sceneclassification-lnhyeqjtn42vqycdtt5jdh.streamlit.app/

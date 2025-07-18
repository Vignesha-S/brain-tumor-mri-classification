# 🧠 Brain Tumor MRI Image Classification

This project uses deep learning techniques to classify brain MRI images into four categories: **glioma**, **meningioma**, **pituitary**, and **no tumor**. The goal is to assist medical professionals in detecting brain tumors accurately and efficiently using automated image classification models.

---

## 🗂️ Project Structure

- `app.py` – Main Streamlit application for real-time prediction
- `utils.py` – Contains helper functions for image preprocessing and model prediction
- `mobilenetv2_best.h5` – Trained MobileNetV2 model for deployment
- `requirements.txt` – Python dependencies required for the project
- `README.md` – Project overview and setup instructions
- `streamlit_ui.jpg` – Screenshot of the Streamlit web application UI

---

## 🔍 Problem Statement

Brain tumors are abnormal growths of cells within the brain that can be life-threatening. Early and accurate diagnosis is crucial. This project aims to automate the classification of brain MRI images into tumor categories using Convolutional Neural Networks (CNNs) and Transfer Learning, reducing the dependency on manual diagnosis.

---

## 🧪 Models Used

1. **Custom CNN Model**
   - Built from scratch using Conv2D, MaxPooling, Dropout, and Dense layers
   - Moderate accuracy; serves as a baseline model

2. **MobileNetV2 (Transfer Learning)**
   - Pretrained on ImageNet, fine-tuned for tumor classification
   - Achieved better accuracy and recall, ideal for deployment

---

## 📈 Results

| Metric               | Custom CNN | MobileNetV2 |
|----------------------|------------|-------------|
| Accuracy             | 71%        | **81%**     |
| Macro F1-Score       | 66%        | **80%**     |
| Meningioma F1 Score  | 0.29       | **0.67**    |
| Pituitary Recall     | 0.98       | **1.00**    |

---

## 🌐 Streamlit Web Application

We built an interactive web app using Streamlit that allows users to upload brain MRI images and view predictions.

### 💡 Features

- **Upload Interface**: Drag & drop or select `.jpg`, `.jpeg`, `.png` images
- **Image Display**: Shows uploaded image for confirmation
- **Prediction Output**: Displays tumor class and confidence score
- **Deployed Model**: Uses MobileNetV2 trained on MRI dataset

### ▶️ To Run the App

```bash
streamlit run app.py

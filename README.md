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

## 🔍 Problem Statementt

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
```



### 📂 Model Files

- `mobilenetv2_best.h5`: Fine-tuned MobileNetV2 model used for prediction.
- `custom_cnn_best.h5`: Custom CNN model trained from scratch (**not uploaded** due to size limitations).

> ℹ️ *Note: Only the MobileNetV2 model is included in the repository since GitHub restricts uploads above 100 MB.*

---

### 🧪 Manual Testing Results

After deployment, several test images were uploaded through the Streamlit app. Below are the observations:

| **Image** | **Expected** | **Predicted** | **Confidence** |
|----------|--------------|----------------|----------------|
| Image 1  | Meningioma   | Meningioma ✅   | 67.25%         |
| Image 2  | Glioma       | Glioma ✅       | 96.35%         |
| Image 3  | No Tumor     | No Tumor ✅     | 93.45%         |
| Image 4  | Pituitary    | Meningioma ❌   | 52.14%         |
| Image 5  | Pituitary    | Pituitary ✅    | 94.15%         |

---

### 🖼️ Streamlit App Screenshot

Below is the user interface of the deployed web application:

![Streamlit UI](https://drive.google.com/uc?id=1IzG0kXP8xaLyH5PSsNLImRxGuuY-ty_p)

---

### ✅ Conclusion

This project successfully demonstrates brain tumor classification using deep learning models. A custom CNN model and a pretrained MobileNetV2 model were developed and evaluated. The MobileNetV2 model outperformed the custom CNN in both accuracy and generalization.

A user-friendly Streamlit web application was created for easy interaction with the model, allowing users to upload MRI images and receive predictions with confidence scores. This real-time interface bridges the gap between deep learning and practical usability, showcasing the potential for deployment in medical diagnostics.

---

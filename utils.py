# -*- coding: utf-8 -*-
"""utils.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pXHeQjS3Xn8kD8K9M9kwmOif3rlVz5Zc
"""

#from google.colab import drive
#drive.mount('/content/drive')

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2

# Load your saved model from Google Drive path
model = load_model("mobilenetv2_best.h5")

# Class names
class_names = ['glioma', 'meningioma', 'no_tumor', 'pituitary']

# Preprocessing function
def preprocess_image(img):
    img = img.resize((224, 224))
    img_array = image.img_to_array(img)
    img_array = img_array / 255.0  # normalize
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Prediction function
def predict_tumor(img):
    img_array = preprocess_image(img)
    prediction = model.predict(img_array)
    confidence = np.max(prediction)
    class_index = np.argmax(prediction)
    return class_names[class_index], confidence
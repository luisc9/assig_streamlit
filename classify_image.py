import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import decode_predictions, preprocess_input

import streamlit as st

import numpy as np
from PIL import Image

model = ResNet50(include_top=True, weights="imagenet")

def classify_image(image):
    img = np.array(image)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)
    img = tf.keras.preprocessing.image.smart_resize(img, size=(224, 224))
    preds = model.predict(img)

    _, class_name, pred_probability = decode_predictions(preds, top=1)[0][0]

    pred_probability = round(float(pred_probability), 4)

    return class_name, pred_probability


# Upload the image
st.title("Image Classification")
uploaded_file = .....

if uploaded_file is not None:
    # Open the image file
    
    # Show the image in the UI
    
    # Make the predictions

    # Print the predictions in the UI

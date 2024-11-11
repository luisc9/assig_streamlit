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
    img = img[:, :, :, :3]
    preds = model.predict(img)

    _, class_name, pred_probability = decode_predictions(preds, top=1)[0][0]

    pred_probability = round(float(pred_probability), 4)

    return class_name, pred_probability


# Upload the image
st.title("Image Classification")
st.write("This webapp takes a dog image and classifies it: it provides a classification and a probability, using the tensorflow, keras and resnet50 libraries and model to predict")
uploaded_file = st.file_uploader("Upload an image file... ", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the image file
    image = Image.open(uploaded_file)
    
    # Show the image in the UI
    st.image(image, "Uploaded image", use_container_width=True)
    
    # Make the predictions
    predicted_name, probability = classify_image(image)

    # Print the predictions in the UI
    st.write(f"Predicted animal = {predicted_name}")
    st.write(f"Probability = {probability}")

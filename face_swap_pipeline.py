import json
import cv2
import numpy as np
from PIL import Image
import insightface
from insightface.app import FaceAnalysis
from insightface.model_zoo import get_model
import matplotlib.pyplot as plt
import os

# Load settings from config.json
with open("config.json", "r") as f:
    config = json.load(f)

SOURCE_IMAGE = config["source_image"]        # Source face image
TARGET_IMAGE = config["target_image"]        # Target image where the face will be swapped in
OUTPUT_IMAGE = config["output_image"]        # Output path for face swap result
SHARPENED_IMAGE = config["sharpened_output"] # Output path for the sharpened result

# Read the images
img = cv2.imread(TARGET_IMAGE)
rob = cv2.imread(SOURCE_IMAGE)

# Check if both images were loaded properly
if img is None or rob is None:
    raise FileNotFoundError("One or both input images could not be loaded.")

# Initialize face detector
app = FaceAnalysis(name='buffalo_l')
app.prepare(ctx_id=0, det_size=(800, 800))

# Detect faces in both images
faces = app.get(img)
rob_faces = app.get(rob)

# Make sure at least one face was detected in the source image
if not rob_faces:
    raise ValueError(f"No face detected in source image ({SOURCE_IMAGE})")

# Use the first detected face from the source image
rob_face = rob_faces[0]

# Load the face swapper model
swapper = get_model('inswapper_128.onnx', download=True)

# Copy the original target image and apply face swap
res = img.copy()
for face in faces:
    res = swapper.get(res, face, rob_face, paste_back=True)

# Convert the result to RGB and save using PIL
res_rgb = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
res_pil = Image.fromarray(res_rgb)
res_pil.save(OUTPUT_IMAGE)
print(f"Face swapped image saved as: {OUTPUT_IMAGE}")

# Define a simple sharpening function using unsharp masking
def sharpen_image(img):
    blurred = cv2.GaussianBlur(img, (0, 0), sigmaX=2)
    return cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

# Load the swapped image and apply sharpening
res_bgr = cv2.imread(OUTPUT_IMAGE)
sharpened = sharpen_image(res_bgr)
cv2.imwrite(SHARPENED_IMAGE, sharpened)
print(f"Sharpened image saved as: {SHARPENED_IMAGE}")

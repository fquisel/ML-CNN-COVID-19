import numpy as np
import os
import cv2
from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

app = Flask(__name__)

labels = ['POSITIVO', 'NEGATIVO']
img_size = 150

model = load_model('model_t1.h5')

def hacer_predicciones(img):
    img = np.reshape(img, (1, img_size, img_size, 1))
    pred = model.predict(img)
    return labels[np.argmax(pred)]

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/", methods = ['POST'])
def prediccion():
    img = request.files['img']
    img_dir = 'static/' + img.filename
    img.save(img_dir)
    img_arr = cv2.imdecode(np.fromstring(img.read(), np.uint8), cv2.IMREAD_GRAYSCALE)
    resized_arr = cv2.resize(img_arr, (img_size, img_size))
    label = hacer_predicciones(resized_arr)
    return render_template("index.html", prediccion = label, imagen = img_dir)

if __name__ == '__main__':
	app.run(debug = True)
import numpy as np
from flask import Flask, render_template, request
from keras.models import load_model
from tensorflow.keras.preprocessing import image

#pip install keras, flask, pillow
#https://colab.research.google.com/drive/1w80SlhJchdJ7Dmi8HmifdxxL-X2hcV2-?usp=sharing

app = Flask(__name__)

dic = {0 : 'Positivo', 1 : 'Negativo'}

model = load_model('model_t1.h5')
model.make_predict_function()

@app.route("/", methods=['GET'])
def main():
    return render_template("index.html")

@app.route("/", methods = ['POST'])
def prediccion():
    img = request.files['img']
    img_dir = 'static/' + img.filename
    img.save(img_dir)
    i = image.load_img(img_dir, target_size=(150,150))
    i = image.img_to_array(i)/255.0
    i = i.reshape(-1,i.shape[0],i.shape[1],1)
    pred = np.argmax(model.predict(i), axis=-1)
    #pred = model.predict_classes(i)
    #pred = pred.reshape(1,-1)[0]
    label = dic[pred[0]]
    #label = '%s (%.2f%%)' % (dic[pred[0]],pred[2]*100)
    return render_template("index.html", prediccion = label, imagen = img_dir)

if __name__ == '__main__':
	app.run(debug = True)
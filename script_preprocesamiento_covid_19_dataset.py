import pandas as pd
import os
import shutil

#lectura y carga de txt
os.chdir('../input')
train_data = pd.read_csv("train.txt",header=None,delim_whitespace=True)
test_data = pd.read_csv("test.txt",header=None,delim_whitespace=True)

#columna filename = nombre de la imagen
#columna class = clase a la que pertenece
train_data.columns = ['patient_id','filename','class','data_source']
test_data.columns = ['patient_id','filename','class','data_source']

#se crea "train_pos_list" que almacena en formato lista el nombre de las imagenes de entrenamiento de clase positiva
pos_train_data = train_data['class'] == 'positive'
pos_train_data = list(train_data[pos_train_data].filename)
print('TRAIN POSITIVO: ',len(pos_train_data))

#se crea "train_neg_list" que almacena en formato lista el nombre de las imagenes de entrenamiento de clase negativa
neg_train_data = train_data['class'] == 'negative'
neg_train_data = list(train_data[neg_train_data].filename)
print('TRAIN NEGATIVO: ',len(neg_train_data))

#se crea "test_pos_list" que almacena en formato lista el nombre de las imagenes de test de clase positiva
pos_test_data = test_data['class'] == 'positive'
pos_test_data = list(test_data[pos_test_data].filename)
print('TEST POSITIVO: ',len(pos_test_data))

#se crea "test_neg_list" que almacena en formato lista el nombre de las imagenes de test de clase negativa
neg_test_data = test_data['class'] == 'negative'
neg_test_data = list(test_data[neg_test_data].filename)
print('TEST POSITIVO: ',len(neg_test_data))

#creación de directorios train y test con subcapeta por clases de imagenes
root_dir = '../output'
posCls = '/POSITIVO'
negCls = '/NEGATIVO'

os.makedirs(root_dir +'/train' + posCls)
os.makedirs(root_dir +'/train' + negCls)
os.makedirs(root_dir +'/test' + posCls)
os.makedirs(root_dir +'/test' + negCls)

#directorio entrada de imagenes carpeta train y test
train_img_dir = os.listdir('../input/train/')
test_img_dir = os.listdir('../input/test/')


for filename in pos_test_data:
    if filename in test_img_dir:
        src = os.path.join('../input/test/', filename) # origen
        dst = os.path.join(root_dir + '/test' + posCls, filename) # destino
        shutil.copy(src,dst)


for filename in neg_test_data:
    if filename in test_img_dir:
        src = os.path.join('../input/test/', filename) # origen
        dst = os.path.join(root_dir + '/test' + negCls, filename) # destino
        shutil.copy(src,dst)


for filename in pos_train_data:
    if filename in train_img_dir:
        src = os.path.join('../input/train/', filename) # origen
        dst = os.path.join(root_dir + '/train' + posCls, filename) # destino
        shutil.copy(src,dst)


for filename in neg_train_data:
    if filename in train_img_dir:
        src = os.path.join('../input/train/', filename) # origen
        dst = os.path.join(root_dir + '/train' + negCls, filename) # destino
        shutil.copy(src,dst)

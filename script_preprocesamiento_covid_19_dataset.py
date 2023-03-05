import pandas as pd
import os
import shutil

def copy_images(src_dir, dst_dir, filenames):
    os.makedirs(dst_dir, exist_ok=True)
    for filename in filenames:
        if filename in os.listdir(src_dir):
            src_path = os.path.join(src_dir, filename)
            dst_path = os.path.join(dst_dir, filename)
            shutil.copy(src_path, dst_path)

# lectura y carga de txt
os.chdir('../input')
train_data = pd.read_csv("train.txt",header=None,delim_whitespace=True)
test_data = pd.read_csv("test.txt",header=None,delim_whitespace=True)
train_data.columns = ['patient_id','filename','class','data_source']
test_data.columns = ['patient_id','filename','class','data_source']

root_dir = '../output'
os.makedirs(os.path.join(root_dir, 'train', 'POSITIVO'), exist_ok=True)
os.makedirs(os.path.join(root_dir, 'train', 'NEGATIVO'), exist_ok=True)
os.makedirs(os.path.join(root_dir, 'test', 'POSITIVO'), exist_ok=True)
os.makedirs(os.path.join(root_dir, 'test', 'NEGATIVO'), exist_ok=True)

train_img_dir = os.listdir('../input/train/')
test_img_dir = os.listdir('../input/test/')

copy_images('../input/test', os.path.join(root_dir, 'test', 'POSITIVO'), test_data[test_data['class'] == 'positive']['filename'])
copy_images('../input/test', os.path.join(root_dir, 'test', 'NEGATIVO'), test_data[test_data['class'] == 'negative']['filename'])

copy_images('../input/train', os.path.join(root_dir, 'train', 'POSITIVO'), train_data[train_data['class'] == 'positive']['filename'])
copy_images('../input/train', os.path.join(root_dir, 'train', 'NEGATIVO'), train_data[train_data['class'] == 'negative']['filename'])

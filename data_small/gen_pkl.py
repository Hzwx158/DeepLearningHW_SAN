import os
import glob
from tqdm import tqdm
import cv2
import pickle as pkl

#用来生成对应的训练/测试所需要的pkl文件
#使用方法：修改path和out即可
#代码原理没有细究
#TODO: 有时间的话稍微写一下原理

#image_path = '/Users/tal/Documents/Tal/myWork/公式识别/code/WAP/data/off_image_train'
#image_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\dataset-from-wan\off_image_train\off_image_train"
image_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\14_test_images\14_test_images"
#image_out = './train_image.pkl'
image_out = './test_image.pkl'
#label_path = 'train_hyb'
label_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\test_caption.txt"
#label_out = './train_label.pkl'
label_out = './test_label.pkl'


images = glob.glob(os.path.join(image_path, '*.bmp'))
image_dict = {}

for item in tqdm(images):

    img = cv2.imread(item)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_dict[os.path.basename(item).replace('_0.bmp','')] = img

with open(image_out,'wb') as f:
    pkl.dump(image_dict, f)

labels = glob.glob(os.path.join(label_path, '*.txt'))
label_dict = {}

for item in tqdm(labels):
    with open(item) as f:
        lines = f.readlines()
    label_dict[os.path.basename(item).replace('.txt','')] = lines

with open(label_out,'wb') as f:
    pkl.dump(label_dict, f)
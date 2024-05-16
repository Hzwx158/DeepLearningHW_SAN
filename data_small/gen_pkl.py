import os
import glob
from tqdm import tqdm
import cv2
import pickle as pkl

'''
    用来生成对应的训练/测试所需要的pkl文件
    使用方法: 修改path和out即可
    请特别注意不要把目录写错(通过assert进行了检查)
'''


#image_path = '/Users/tal/Documents/Tal/myWork/公式识别/code/WAP/data/off_image_train'
#image_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\dataset-from-wan\off_image_train\off_image_train"
#image_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\a_matched_test_set\14_test_images\14_test_images"
#image_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\HME100K\HME100K\train\train_images"
image_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\HME100K\HME100K\test\test_images"

#image_out = './train_image.pkl'
image_out = './test_image.pkl'

#label_path = 'train_hyb'
#label_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\HME100K\HME100K\train"
label_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\HME100K\HME100K\test"
#label_path = r"E:\pythonwork\deep_learning\big_homework\SAN-main\data\a_matched_test_set"

#label_out = './train_label.pkl'
label_out = './test_label.pkl'


subfix = 'jpg'
images = glob.glob(os.path.join(image_path, f'*.{subfix}'))
image_dict = {}
assert len(images)!=0, "empty images"
for item in tqdm(images):

    img = cv2.imread(item)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #image_dict[os.path.basename(item).replace(f'_0.{subfix}','')] = img
    image_dict[os.path.basename(item).replace(f'.{subfix}','')] = img

with open(image_out,'wb') as f:
    pkl.dump(image_dict, f)

labels = glob.glob(os.path.join(label_path, '*.txt'))
assert len(labels)!=0, "empty labels!"
label_dict = {}

#测试集中含有中文顿号，需要用utf-8， 否则会报错
for item in tqdm(labels):
    with open(item, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    label_dict[os.path.basename(item).replace('.txt','')] = lines

with open(label_out,'wb') as f:
    pkl.dump(label_dict, f)
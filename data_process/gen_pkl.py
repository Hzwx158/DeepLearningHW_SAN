import os
import glob
from tqdm import tqdm
import cv2
import pickle as pkl
from pathlib import Path

'''
    用来生成对应的训练/测试所需要的pkl文件
    使用方法: 修改path和out即可
    请特别注意不要把目录写错(通过assert进行了检查)
'''

mode = 'train'
#image_path = '/Users/tal/Documents/Tal/myWork/公式识别/code/WAP/data/off_image_train'
DATA_FOLDER = (Path(__file__).parents[1]/'data').absolute()
assert DATA_FOLDER.exists()
image_path = str(DATA_FOLDER/("off_image_%s/off_image_%s"%(mode, mode)))
image_out = str(DATA_FOLDER/('%s_image.pkl'%mode))

#label_path = 'train_hyb'
label_path = str(DATA_FOLDER/("%s_hyb"%mode))
label_out = str(DATA_FOLDER/('%s_label.pkl'%mode))


subfix = 'bmp'
images = glob.glob(os.path.join(image_path, f'*.{subfix}'))
image_dict = {}
assert len(images)!=0, "empty images"
for item in tqdm(images):

    img = cv2.imread(item)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    image_dict[os.path.basename(item).replace(f'_0.{subfix}','')] = img
    # image_dict[os.path.basename(item).replace(f'.{subfix}','')] = img

with open(image_out,'wb') as f:
    pkl.dump(image_dict, f)

labels = glob.glob(os.path.join(label_path, '*.txt'))
assert len(labels)!=0, "empty labels!"
assert len(labels)==len(images), 'number of labels is not equal to number of images'
label_dict = {}

# 原来的gen_pkl不适合我们找的数据集
for item in tqdm(labels):
    with open(item, 'r') as f:
        lines = f.readlines()
    label_dict[os.path.basename(item).replace('.txt','')] = lines

with open(label_out,'wb') as f:
    pkl.dump(label_dict, f)
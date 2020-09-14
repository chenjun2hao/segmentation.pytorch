import glob
from PIL import Image
import json
import random
import numpy as np

data_name = 'Person'
img_folder = '/home/data/CM/data/Segmentation/SuperviselyPersonDataset/imgs/*/*/*.png'

datas = glob.glob(img_folder)
img_folder = '/home/data/CM/data/Segmentation/SuperviselyPersonDataset/imgs/*/*/*.jpeg'
datas2 = glob.glob(img_folder)

datas = datas + datas2
train = []

with open('./data/Person/training.odgt', 'w') as f:
    for data in datas:
        per_path = data.split('/')

        path = 'Person/person/' + '/'.join(per_path[-4:])
        label = 'Person/person/labels/' + per_path[-3] + '/' + per_path[-1]

        img = Image.open(data)
        w,h = img.size

        contend = {}
        contend['fpath_img'] = path
        contend['fpath_segm'] = label
        contend['width'] = w
        contend['height'] = h

        contend = json.dumps(contend) + '\n'
        train.append(contend)

        # f.write(contend)
        f.writelines(contend)
        f.flush()


with open('./data/Person/validation.odgt', 'w') as f:
    val = random.sample(train, 1000)

    for per_val in val:
        f.write(per_val)
        f.flush()
import os
import cv2
import numpy as np
import sys
sys.path.append('../')
from src.landmarks import Landmarks

def read_folder(path, images = 'images', labels = False, landmarks = False, n = None, RGB = False):
    items_paths = list(item.path for item in os.scandir(f'{path}/{images}'))
    images = {}
    if n is None:
        n = len(items_paths)
    for i in range(n): 
        filename = os.path.basename(os.path.splitext(items_paths[i])[0])
        if RGB:
            img = cv2.cvtColor(cv2.imread(items_paths[i]), cv2.COLOR_BGR2RGB)
        else:
            img = cv2.imread(items_paths[i])
        images[filename] = {'img': img}
    if labels != False:
        for key in images:
            images[key]['labels'] = cv2.imread(f'{path}/{labels}/{key}.png')
    if landmarks != False:
        for key in images:
            with open(f'{path}/{landmarks}/{key}.txt') as f:
                landmark = [line[:-1].split(' ') for line in f][1:]
            images[key]['landmarks'] = Landmarks(np.array(landmark).astype(float))
    return images
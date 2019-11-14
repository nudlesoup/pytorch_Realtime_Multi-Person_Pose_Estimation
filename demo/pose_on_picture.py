import os
import re
import sys
import cv2
import math
import time
import scipy
import argparse
import matplotlib
import numpy as np
import pylab as plt
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from collections import OrderedDict
from scipy.ndimage.morphology import generate_binary_structure
from scipy.ndimage.filters import gaussian_filter, maximum_filter

from lib.network.rtpose_vgg import get_model
from lib.network import im_transform
from evaluate.coco_eval import get_outputs, handle_paf_and_heat
from lib.utils.common import Human, BodyPart, CocoPart, CocoColors, CocoPairsRender, draw_humans
from lib.utils.paf_to_pose import paf_to_pose_cpp
from lib.config import cfg, update_config

parser = argparse.ArgumentParser()
# parser.add_argument('--cfg', help='experiment configure file name',
#                    default='./experiments/vgg19_368x368_sgd.yaml', type=str)
# parser.add_argument('--weight', type=str,
#                    default='/home/tensorboy/Downloads/pose_model.pth')
# parser.add_argument('opts',
#                    help="Modify config options using the command-line",
#                    default=None,
#                    nargs=argparse.REMAINDER)
parser.add_argument('--cfg', help='experiment configure file name', default='/home/nudlesoup/Research'
                                                                            '/pytorch_Realtime_Multi'
                                                                            '-Person_Pose_Estimation/experiments'
                                                                            '/vgg19_368x368_sgd.yaml', type=str)
parser.add_argument('--weight', type=str, default='/home/nudlesoup/Downloads/pose_model.pth')
parser.add_argument('opts',
                    help="Modify config options using the command-line",
                    default=None,
                    nargs=argparse.REMAINDER)
args = parser.parse_args()

# update config file
update_config(cfg, args)

weight_name = '/home/nudlesoup/Downloads/pose_model.pth'

model = get_model('vgg19')
model.load_state_dict(torch.load(weight_name))
model = torch.nn.DataParallel(model).cuda()
model.float()
model.eval()

#test_image = '/home/nudlesoup/Research/pytorch_Realtime_Multi-Person_Pose_Estimation/readme/trial3.jpg'
dirName = '/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricImages'
outputPath = '/home/nudlesoup/Research/MakingImagesfromDataset/NonEgoCentricPoseImages'
for (dirpath, dirnames, filenames) in os.walk(dirName):
    structure = os.path.join(outputPath, dirpath[len(dirName)+1:])
    print(structure)
    if not os.path.isdir(structure):
        os.mkdir(structure)
    else:
        print("Folder does already exits!")


for (dirpath, dirnames, filenames) in os.walk(dirName):
    for file in filenames:
        my_file = os.path.join(outputPath, dirpath[len(dirName) + 1:],file)
        if os.path.isfile(my_file):
            continue
        else:
            full_file_name = os.path.join(dirpath, file)
            if os.path.isfile(full_file_name):
                oriImg = cv2.imread(full_file_name)  # B,G,R order
                shape_dst = np.min(oriImg.shape[0:2])
            else:
                print("full_file_name is : " + full_file_name)
                break
            # Get results of original image

            with torch.no_grad():
                paf, heatmap, im_scale = get_outputs(oriImg, model, 'rtpose')

            print(im_scale)
            humans = paf_to_pose_cpp(heatmap, paf, cfg)

            out = draw_humans(oriImg, humans)
            outputFileName = os.path.join(outputPath, dirpath[len(dirName) + 1:],file)
            cv2.imwrite(outputFileName, out)


import torch as tc
import torchvision as tv
import torchvision.transforms as transforms
import torchvision.datasets as dsets
import torch.nn as nn
import torch.nn.functional as F
import cv2
import numpy as np


USE_CUDA=tc.cuda.is_available()
print(USE_CUDA)
device=tc.device('cuda:0'if USE_CUDA else 'cpu')
print('device:',device)


#src=cv2.imread("./Dataset/tiles-resized/{}.jpg".format(i),flags=cv2.IMREAD_COLOR)
learning_rate = 0.001
training_epochs = 15
batch_size = 100

train_data=dsets.DatasetFolder("./Dataset/tiles-resized",train=True,)

class CNN(nn.module):
    def __init__(self):
        super(CNN,self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=(3, 3), stride=1, padding=(1, 1)),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 2), stride=2))

        self.layer2 = nn.Sequential(
            nn.Conv2d(32, 64, kernel_size=(3, 3), stride=1, padding=(1, 1)),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=(2, 2), stride=2))

        self.fc = nn.Linear(50*50*64, num_types, bias=True)

        nn.init.xavier_uniform_(self.fc.weight)

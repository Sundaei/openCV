from PIL import Image
import matplotlib
import matplotlib.pyplot as plt
import torch
from torch.utils.data import Dataset, dataloader
import numpy as np
import torchvision
from torchvision import transforms

trans=transforms.Compose([transforms.Resize((100,100)),transforms.ToTensor(),transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))])
trainset=torchvision.datasets.ImageFolder(root="./Dataset/1",transform=trans)

#print(trainset.__getitem__(3))
print(len(trainset))
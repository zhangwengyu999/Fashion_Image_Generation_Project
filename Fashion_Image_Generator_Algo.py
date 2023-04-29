#############################################################################
# COMP4423 – Computer Vision                                                #
# Group Project: Fashion Image Generation                                   #
#                                                                           #
# Group 1                                                                   #
#                                                                           #
# JIANG Yiyang (21095707d)                                                  # 
# YE Haowen (21098829d)                                                     #
# ZHANG Wengyu (21098431d)                                                  #
#                                                                           #
# This is the Algorithm program for the Project                             #
#                                                                           #
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   #
#   !! Please carefully read User_Manual.pdf file first before running !!   #
#   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!   #
#                                                                           #
#############################################################################

import torch
import numpy as np
from torch import nn
import matplotlib.pyplot as plt
from torchvision.utils import make_grid

# Define the Generator and Discriminator
class Generator(nn.Module):
    def __init__(self):
        super(Generator,self).__init__()
        self.label_embed = nn.Embedding(10,100)
        
        self.model = nn.Sequential(
            # 100 1 1
            nn.ConvTranspose2d(100,512,4,1,0,bias = False),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            
            # 512 4 4
            nn.ConvTranspose2d(512,256,4,2,1,bias = False),
            nn.BatchNorm2d(256),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            
            # 256 8 8
            nn.ConvTranspose2d(256,128,4,2,1,bias = False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            
            # 128 16 16
            nn.ConvTranspose2d(128,64,4,2,1,bias = False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2, inplace=True),
            nn.Dropout(0.3),
            
            # 64 32 32
            nn.ConvTranspose2d(64,1,4,2,1,bias = False),
            nn.Flatten(),
            # 1 64 64
            nn.Linear(1*64*64, 1*28*28),
            # 1 28 28
            nn.Tanh()
        )
    
    def forward(self,X,label):
        label = self.label_embed(label)
        x = torch.mul(X,label)
        x = x.view(-1,100,1,1)
        x = self.model(x)
        return x.view(-1,1,28,28)

class Discriminator(nn.Module):
    
    def __init__(self):
        super(Discriminator,self).__init__()        
        
        self.model = nn.Sequential(
            # 1 28 28
            nn.Conv2d(1,64,4,2,1,bias = False),
            nn.BatchNorm2d(64),
            nn.LeakyReLU(0.2,True),
            nn.Dropout2d(0.5),
            
            # 64 14 14
            nn.Conv2d(64,128,4,2,1,bias = False),
            nn.BatchNorm2d(128),
            nn.LeakyReLU(0.2,True),
            nn.Dropout2d(0.5) 
            # 128 7 7
        )
        
        self.D_layer = nn.Sequential(
            nn.Conv2d(128,1,7,1,0,bias = False), 
            # 128 7 7 -> 1                                   
            nn.Sigmoid())
        
        self.class_layer = nn.Sequential(
            nn.Conv2d(128,11,7,1,0,bias = False), # 11th label: 'fake'
            # 128 7 7 -> 11
            nn.LogSoftmax(dim = 1))
        
    def forward(self,X):
        x = self.model(X)        
        dis = self.D_layer(x).view(-1)
        cla = self.class_layer(x).view(-1,11)
        return dis,cla

labelMap = ['T-Shirt', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# generate N images from a label
def generateFromLabel(inLabel, inNum):
    loadPath = 'ACGAN6_G_30_1.pth'
    device = torch.device('cpu')
    inG = torch.load(loadPath, map_location=device)
    inG.eval()
    random = torch.randn(inNum, 100).to(device)
    random_labels = np.array([i for _ in range(1) for i in [inLabel]*inNum])
    random_labels = torch.from_numpy(random_labels).int().to(device)
    output  = inG.forward(random, random_labels).unsqueeze(1).data.to(device)
    output = output.view(inNum, 1, 28, 28)
    grid = make_grid(output, nrow=inNum, normalize=True).permute(1,2,0).cpu().numpy()
    return grid

# for testing
if __name__ == '__main__':
    l = 9
    n = 10
    img = generateFromLabel(l, n)
    fig, ax = plt.subplots(figsize=(n,n))
    ax.imshow(img)
    plt.title('Generated ['+labelMap[l]+'] Fashion Images')
    plt.axis('off')
    plt.show()
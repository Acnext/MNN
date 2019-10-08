import torch
import numpy as np
from torch.utils.data import Dataset
class textdata(Dataset):
    def __init__(self, filename, total):
        self.len = total
        file = open(filename, 'r')
        sum = 0
        for line in file:
            id = int(line[0 : line.find(' ')])
            
    def __len__(self):
        return self.len
    def __getitem__(self, index):
        
        
    

import torch
import pandas as pd
import torch.nn as nn
from config import DATA
import torch.nn.functional as F
from sklearn.model_selection import train_test_split


class Model(nn.Module):

    def __init__(self,in_feature=3,h1=8,h2=9,out_features=3):
        super().__init__()
        self.fc1 = nn.Linear(in_feature,h1)
        self.fc2 = nn.Linear(h1,h2)
        self.out = nn.Linear(h2,out_features)


    def forward(self,x):

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.out(x)

        return x


if __name__ == "__main__":
    df = pd.read_csv(DATA)
    X = df.drop('variety',axis=1)
    y = df['variety']
    X = X.values
    y = y.values
    X_train , X_test , y_train , y_test = train_test_split(X,y,test_size = .2, random_stat = 33)
    X_train = torch.FloatTensor(X_train)

    X_test = torch.FloatTensor(X_test)
    torch.manual_seed(32)
    model = Model()





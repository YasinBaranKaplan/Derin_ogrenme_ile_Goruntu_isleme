# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 20:59:27 2024

@author: kapla
"""

import glob
import os 
import numpy as np 
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten ,Conv2D, MaxPooling2D
from PIL import Image
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
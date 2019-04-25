import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from keras.datasets import mnist
import numpy as np
from keras import metrics
from keras.models import Model
from keras.layers import Input, Dense
from keras import regularizers
import os
import gzip
import numpy as np
import pickle

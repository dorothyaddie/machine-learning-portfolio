#import block
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from sklearn.model_selection import train_test_split
from IPython.display import Image 
from pydot import graph_from_dot_data
from six import StringIO
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
import comparing_models

arr = np.array([1, 2, 3, 4, 5])
project_data = pd.read_csv("data.csv")
project_numpy = project_data.to_numpy()
input = project_numpy[:,:-1]
output = project_numpy[:,-1]

#checks that dimension was actually reduced to two dimensions
def test_two_dim_shape():
	out = comparing_models.two_dim(project_data)
	assert out.shape[1] == 2

#checks the type of dimension reduction
def test_two_dim_type():
	out = comparing_models.two_dim(project_data)
	assert type(out) == type(arr)

#checks that input is 13 columns 
def test_input_shape():
    out = input
    assert out.shape[1] == 13

#checks that output is 1 column
def test_output_shape():
    out = output
    assert out.shape[0] == 195

def test_input_type():
    out = input
    assert type(out) == type(arr)

def test_output_type():
    out = output
    assert type(out) == type(arr)



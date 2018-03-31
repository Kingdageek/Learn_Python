#kNN.py
from numpy import *
import operator

def createDataSet():
    group = array([[1.0,1.1],
                  [1.0,1.0],
                  [0,0],
                  [0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

"""
def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize,1)) - dataSet
    sqdiffMat = diffMat ** 2
    sqDistances = sqdiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndices = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndices[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) +1
    sortedClassCount = sorted(classCount.items(), key= operator.itemgetter(1), 
                              reverse=True)
    return sortedClassCount[0][0]
"""

def classify0(inX, dataset, labels, k):
    # we want to make our new data instance the same shape with our dataset
    # array. We need to get the size of dataset and use it as a multiplicative
    # factor to make inX match dataset in order to obtain the distances of all
    # the dataset points and inX
    dataset_size = dataset.shape[0]
    new_inX = tile(inX, (dataset_size, 1))
    diff_arr = dataset - new_inX
    # Euclidean distance btw 2 points
    sq_arr = diff_arr ** 2
    # To sum delta(x) and delta(y)
    sum_arr = sq_arr.sum(axis=1) # add along the rows. Add points x to y
                        # forming a new array having 1 column
    dist_arr = sum_arr ** 0.5 # square root
    # we need to obtain the sorted indices of dist_arr to use to access labels
    # to know the class inX has the shortest distance to.
    sorted_indices = dist_arr.argsort()
    count_class = {} # accumulator dictionary
    for i in range(k):
        l = labels[sorted_indices[k]] # which labels made our k cut
        count_class[l] = count_class.get(l,0) + 1
    sorted_list = sorted(count_class.items(), key = operator.itemgetter(1),
                         reverse=True)
    # reverse set to true to obtain most occurring label
    return sorted_list[0][0]

# To parse text file - datingTestSet.txt to data classifier can understand

def file_2_array(file):
    with open(file) as f:
        fl = f.readlines()
    fls = len(fl)
    # An array of zeros with dimension of training set we'll soon fill with data
    # from file. 3 features (3 columns), Each data instance is on a line so,
    # no. of rows = len(f.readlines())
    training_arr = zeros(fls, 3)
    class_arr = []
    # Do this for as long as there are lines in f
    for i in range(fls):
        line = fl[i].strip() # strip every preceding or following spaces & "\n"
        line_li = line.split("\t") # split line with tabs
        training_arr[i] = line_li[0:3] # fill the ith row of training_arr with
                            # 1st 3 elements of line_li (our 3 features)
        class_arr.append(int(line_li[-1]))
    return training_arr, class_arr
    
    

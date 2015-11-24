__author__ = 'zzwwws'
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt

def createDataSet():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels

def classify(inX, dataSet, labels, k):
    dataSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSize,1)) - dataSet
    sqDiffMat = diffMat ** 2
    #axis = 0 sum row, axis = 1 sum column
    sqDistance = sqDiffMat.sum(axis=1)
    distance = sqDistance ** 0.5
    sortdistance = distance.argsort()
    classcount = {}
    for i in range(k):
        votelLabels = labels[sortdistance[i]]
        classcount[votelLabels] = classcount.get(votelLabels,0) + 1
    sortedClassCount = sorted(classcount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def file2Matrix(filename):
    fr = open(filename)
    arrayOLines = fr.readlines()
    numberOfLines = len(arrayOLines)
    returnMat = zeros((numberOfLines,3))
    classLabelVector = []
    index = 0
    for line in arrayOLines:
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(int(float(listFromLine[2])/0.1))
        index += 1
    return returnMat, classLabelVector
datingDataMat, datingLabels = file2Matrix('datingTestSet.txt')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 15 * array(datingLabels), 15 * array(datingLabels))
plt.show()

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:07:12 2016

@author: guxh
"""

import numpy as np


def quarter(items):
    return items[int(len(items) * 0.25)]
    
def threeQuarters(items):
    return items[int(len(items) * 0.75)]

def maxMinuxMin(items):
    return items[-1] - items[0]    


def getCommonFeatures(directCommonFeatures, items, year, month):
    key = year + '-' + month + ',' + items[1]
    
    if key not in directCommonFeatures:
        directCommonFeatures[key] = []
        for i in range(6):
            directCommonFeatures[key].append([])

    for i, j in zip(range(6), (7, 8, 10, 13, 17, 22)):
        directCommonFeatures[key][i].append(float(items[j]))

def generateindirectCommonFeatures(directCommonFeatures, indirectCommonFeatures):
    functions = [np.sum, np.average, quarter, np.median, threeQuarters, np.std, maxMinuxMin]
    
    for key in directCommonFeatures:
        indirectCommonFeatures[key] = []
        
        for i in range(6):
            indirectCommonFeatures[key].append([])
            
            if len(directCommonFeatures[key][i]) < 30:
                directCommonFeatures[key][i] += [0] * (30 - len(directCommonFeatures[key][i]))
            directCommonFeatures[key][i].sort()
            
            for func in functions:
                indirectCommonFeatures[key][i].append(func(directCommonFeatures[key][i]))

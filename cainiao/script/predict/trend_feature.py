# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:07:12 2016

@author: guxh
"""

year_month = {
    '2014-10' : '2014-11,',
    '2014-11' : '2015-01,',
    '2015-03' : '2015-04,',
    '2015-04' : '2015-05,',
    '2015-05' : '2015-06,',
    '2015-06' : '2015-07,',
    '2015-07' : '2015-08,',
    '2015-08' : '2015-09,',
    '2015-09' : '2015-10,',
    '2015-10' : '2015-11,'
}


def getTrendFeatures(directTrendFeatures, items, year, month):
    key = year + '-' + month + ',' + items[1]
    date = int(items[0][-2:])
    index = 0 if date <= 10 else (1 if date <= 20 else 2)

    if key not in directTrendFeatures:
        directTrendFeatures[key] = []
        for i in range(5):
            directTrendFeatures[key].append([0.0, 0.0, 0.0])
        # directTrendFeatures[key].append(0.0)

    for i, j in zip(range(5), (7, 8, 10, 13, 17)):
        directTrendFeatures[key][i][index] += float(items[j])
    # if date <= 14:
        # directTrendFeatures[key][5] += float(items[29])


def generateIndirectTrendFeatures(directTrendFeatures, indirectTrendFeatures):
    for key in directTrendFeatures:
        indirectTrendFeatures[key] = []
        directFeatures = directTrendFeatures[key]
        
        for i in range(5):
            for j in (1,2):
                indirectTrendFeatures[key].append(directFeatures[i][j] - directFeatures[i][j-1])

        # indirectTrendFeatures[key].append(directFeatures[5])
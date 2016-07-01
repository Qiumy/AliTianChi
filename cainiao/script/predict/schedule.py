# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 10:27:39 2016

@author: guxh
"""

import csv
import common_feature
import trend_feature

def getFeaturesPerMonth(year, month, directCommonFeatures, directTrendFeatures):
    prefixOfFileName = 'D:/somecompetition/tianchi/all/date/' + year + month
    dictRange = {'11' : range(128, 131), '12' : range(101, 127)}
    days = dictRange[month]
    for day in days:
        day = str(day)[1:]
        fileName = prefixOfFileName + day + '.csv'
        getFeaturesPerDay(directCommonFeatures, directTrendFeatures, fileName, year, month)
        
        
def getFeaturesPerDay(directCommonFeatures, directTrendFeatures, fileName, year, month):
    with open(fileName) as f:
        reader = csv.reader(f)
        reader.next()
        for items in reader:
            if items[0] == 'date':
                continue
            common_feature.getCommonFeatures(directCommonFeatures, items, year, month)
            trend_feature.getTrendFeatures(directTrendFeatures, items, year, month)
            
def outputFeatures(ourputFileName, indirectCommonFeatures, indirectTrendFeatures):
    with open(outputFileName, 'w') as f:
        for key in indirectCommonFeatures:
            f.write(key)
            for value in indirectCommonFeatures[key]:
                f.write(',' + ','.join(map(str, value)))
            f.write(',' + ','.join(map(str, indirectTrendFeatures[key])))
            f.write('\n')

            
if __name__ == '__main__':
    year_month = (('2015', '11'), ('2015', '12'))
    outputFileName = 'D:/somecompetition/tianchi/result/predict.csv'
    directCommonFeatures = {}
    directTrendFeatures = {}
    indirectCommonFeatures = {}
    indirectTrendFeatures = {}
    
    for year, month in year_month:
        getFeaturesPerMonth(year, month, directCommonFeatures, directTrendFeatures)

    common_feature.generateindirectCommonFeatures(directCommonFeatures, indirectCommonFeatures)
    trend_feature.generateIndirectTrendFeatures(directTrendFeatures, indirectTrendFeatures)
    outputFeatures(outputFileName, indirectCommonFeatures, indirectTrendFeatures)
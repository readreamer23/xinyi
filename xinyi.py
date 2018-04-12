# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import os 
#import codecs
import glob
import json
import pandas as pd
from pandas import DataFrame,Series

result = []
all_entity = []

os.getcwd()
os.chdir(r'E:\宋心艺\xinyi')

files=glob.glob('*.json')

for filename in files:
    str1 = '_'
    end = filename.find(str1)
    number = filename[0:end]
    
    domain = os.path.abspath(r'E:\宋心艺\xinyi')
    filepath = os.path.join(domain,filename)
    
    f = open(filepath,encoding="utf-8")
    info = json.load(f)
    
    str = '\n'
    info['entity'] = list(filter(lambda x: x.count(str)==0 , info['entity']))
    
    all_entity.extend(info['entity'])

obj = pd.Series(all_entity)
#print(obj)
obj.to_csv(r'E:\宋心艺\result\xinyi_obj.csv',encoding = 'utf-8')    

##########################################################   
    info['number'] = number
    name = ['title','number','entity','summary']
    data = pd.Series(info,index=name)
    #print(data)
    #print(data['title'],data['entity'],data['summary'])
    result.append(data)
    
#print(result)
result2 = pd.DataFrame(result)
#print(result2)
result2.to_csv(r'E:\宋心艺\result\xinyi.csv',index = False,encoding = 'utf-8')

"""
统计实体词的个数
"""
obj = pd.Series(all_entity)
#print(obj)     
obj_count = obj.value_counts()
#print(obj_count)
obj_count.to_csv(r'E:\宋心艺\result\xinyi_obj_count.csv',encoding = 'utf-8')
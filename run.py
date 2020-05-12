#!/usr/bin/env python3
import os
import requests

file_dir = 'supplier-data/images/'
url = 'http://localhost/fruits/'
files = os.listdir(file_dir)
for file in files:
    if not file.endswith('.jpeg'):
        continue
    data = {}
    name = file.split('.',1)[0]
    with open('supplier-data/descriptions/'+name+'.txt') as text_file:
        data['name']=text_file.readline().replace('\n','')
        data['weight']=int(text_file.readline().replace('\n','').split(' ',1)[0])
        data['description']=text_file.readline().replace('\n','')
        data['image_name']=file
        r = requests.post(url, data = data)

#!/usr/bin/env python3
import os
from PIL import Image
dir = 'supplier-data/images/'
files = os.listdir(dir)
for file in files:
    if not file.endswith('.tiff'):
        continue
    img = Image.open(dir+file)
    name = file.split('.',1)[0]
    img = img.convert('RGB')
    img = img.resize((600,400))
    img.save(dir+name+'.jpeg')


#!/usr/bin/env python3

import requests
import os
url = 'http://localhost/upload/'
file_dir = 'supplier-data/images/'
files = os.listdir(file_dir)
for file in files:
    if not file.endswith('.jpeg'):
        continue
    with open(file_dir+file, 'rb') as opened:
        r = requests.post(url, files={'file':opened})

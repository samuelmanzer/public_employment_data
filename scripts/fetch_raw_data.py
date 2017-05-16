#!/usr/bin/env python

import requests
import os

# We need to get some cookies before we directly 
# our target file
establish_session_req = requests.get('https://www.opm.gov/data/')

data_file_req = requests.get('https://www.opm.gov/Data/Files/425/fdb8db0d-ce56-4966-9572-9692e6e0fa5e.zip')

data_file_dir = './data/fedscope/2016_03/'
if not os.path.exists(data_file_dir):
    os.makedirs(data_file_dir)

data_file_path = data_file_dir + 'raw.zip'
data_file = open(data_file_path, 'wb')
data_file.write(data_file_req.content)
data_file.close()

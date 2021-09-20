#!/usr/bin/env python

import requests
import pandas as pd

# list of gh usernames
users = ['asummerville', 
        'Ryphilen', 
        'tic', 
        'tballard34', 
        'Kalvinci',
        'jackieannec', 
        'aparnakishore', 
        'katiemartins', 
        'sidman00', 
        'vgcecchetti', 
        'kothmann1', 
        'Mikokokokoto', 
        'ShahiHub', 
        'elixir-1'
        ]

# create empty df
col_names = ['username', 'sesame', 'rps', 'sleep']
df = pd.DataFrame(columns = col_names)

# loop through the repos
# add error handling -- repo name, Readme vs readme
def parse():
    for user in users:
        username = user
        sesame = 's'
        rps = 'r'
        sleep = 's'
        # try pulling a user's readme file from their repo --either health or healthy-- if fails, they didn't complete the assignment
        try:
            r = requests.get(f'https://raw.githubusercontent.com/{username}/smart_and_health_buildings/main/lab_1/readme.md')
            content = r.text
            print(content)
            #parse content into df
            df = df.append({'username':username, 'sesame':sesame, 'rps':rps, 'sleep':sleep}, ignore_index=True)
        except requests.HTTPError as exception:
            r = requests.get(f'https://raw.githubusercontent.com/{username}/smart_and_healthy_buildings/main/lab_1/readme.md')
            content = r.text
            print(content)
            #parse content into df
            df = df.append({'username':username, 'sesame':sesame, 'rps':rps, 'sleep':sleep}, ignore_index=True)
        except:
            df = df.append({'username':username, 'sesame':null, 'rps':null, 'sleep':null}, ignore_index=True)
        
        df

if __name__ == '__main__':
    parse()
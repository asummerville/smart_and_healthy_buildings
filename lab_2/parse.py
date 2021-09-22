#!/usr/bin/env python

## DOESN'T QUITE WORK
## student submissions very inconsistent

import requests
import pandas as pd
import numpy as np

# loop through the repos
# add error handling -- repo name, Readme vs readme

def parse(content, df, user):
    try:
        print('reached parse fxn try')
        c = content.split('\n')
        list_items = [i for i in c if '-' in i]
        sesame = list_items[0].strip().strip('-').strip( )
        rps = list_items[1].strip().strip('-').strip( )
        sleep = list_items[2].strip().strip('-').strip( )
        print('reached df append')
        df = df.append({'username':user, 'sesame':sesame, 'rps':rps, 'sleep':sleep}, ignore_index=True)
    except:
        df = df.append({'username':user, 'sesame':np.nan, 'rps':np.nan, 'sleep':np.nan}, ignore_index=True)

def main():

    # list of gh usernames
    users = ['testusers', 'asummerville', 'Ryphilen', 'tic', 'tballard34', 'Kalvinci','jackieannec', 'aparnakishore', 'katiemartins', 'sidman00', 'vgcecchetti', 'kothmann1', 'Mikokokokoto', 'ShahiHub', 'elixir-1']

    # create empty df
    col_names = ['username', 'sesame', 'rps', 'sleep']
    df = pd.DataFrame(columns = col_names)

    for user in users:

        # try pulling a user's readme file from their repo --either health or healthy-- if fails, they didn't complete the assignment
        r = requests.get(f'https://raw.githubusercontent.com/{user}/smart_and_health_buildings/main/lab_1/readme.md')
        content = r.text
        if content == '404: Not Found':
            r = requests.get(f'https://raw.githubusercontent.com/{user}/smart_and_health_buildings/master/lab_1/readme.md')
            content = r.text
            if content == '404: Not Found':
                r = requests.get(f'https://raw.githubusercontent.com/{user}/smart_and_healthy_buildings/main/lab_1/readme.md')
                content = r.text
                if content == '404: Not Found':
                    r = requests.get(f'https://raw.githubusercontent.com/{user}/smart_and_healthy_buildings/master/lab_1/readme.md')
                    content = r.text
                    df = df.append({'username':user, 'sesame':np.nan, 'rps':np.nan, 'sleep':np.nan}, ignore_index=True)
                else:
                    parse(content, df, user)
            else:
                print('reached correct parse fxn')
                parse(content, df, user)
        else:
            parse(content, df, user)
    
    print(df)

if __name__ == '__main__':
    main()
import os
import glob
import pandas as pd



def searchFolder(path=None, *args):
    '''
    Search a value within a folder of csv files.
       
    If searching multiple values, separate each value by commas
    '''
    path = input("Enter folder name: ")
    args = input("Enter search value(s): ").split(',')
    for p, dirnames, filenames in os.walk('/'):
        if path in dirnames:
            p = p + '\\' + path
            break
        else:
            continue
    try:
        df = pd.concat([pd.read_csv(file) for file in 
             glob.iglob('{}/*'.format(p))])

        cls = df[df.isin([x for x in args]).any(1)]
        print('\n',cls)
    except pd.errors.ParserError as e:
        print('Folder not found')
        pass

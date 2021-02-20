import glob
import pandas as pd




def searchFolder(path, *args):
    '''
    Search value(s) within a folder of csv files.

    If searching multiple values, separate each value by commas



    Parameters
    ----------
    path: folder name (not full path)

    args: value(s)


    Returns
    ----------
    cls: pandas dataframe


    Examples
    ----------
    >>> from searcherGuy import searchFolder
    >>> searchFolder('foo', 'bar', 'foobar')
    pd.DataFrame

    '''

    try:
        df = pd.concat([pd.read_csv(file) for file in 
             glob.iglob('{}/*'.format(path))])

        cls = df[df.isin([x for x in args]).any(1)]
        display(cls)
    except pd.errors.ParserError as e:
        print('Folder not found')
        pass
    
    
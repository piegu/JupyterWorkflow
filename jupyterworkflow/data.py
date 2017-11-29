import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'
PATH = 'data/'

def get_fremont_data(path=PATH,filename="Fremont.csv",
			url=FREMONT_URL, force_download=False):
    """Download the Fremont data

    Parameters
    ----------
    path : string (optional)
       the path to csv file
    filename : string (optional)
        location to save the data
    url : string (optional)
        web location of the data
    force_download : bool (optional)
        if True, force the redownload of data

    Returns
    -------
    pandas.DataFrame
        the Fremont Bridge data
    """
    file = path+filename
    if force_download or not os.path.exists(file):
        urlretrieve(url, file) 
    data = pd.read_csv(file, index_col='Date', parse_dates=True)
    data.columns = ['W', 'E']
    data['Total'] = data['W'] + data['E']
    return data

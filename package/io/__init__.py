import functools

import pandas as pd


@functools.lru_cache(maxsize=1)
def load_csv(filepath):
    print(f'Load Csv:{filepath}')
    data=pd.read_csv(filepath)
    print('Load Success')
    return data

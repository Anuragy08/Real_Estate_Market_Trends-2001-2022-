# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 16:42:49 2025

@author: anura
"""

import pandas as pd

def read_split_files(file_paths):
    """
    Given a list of file paths, reads them into DataFrames.

    Returns:
        List of DataFrames [df1, df2, ...]
    """
    dfs = []
    

    for i, path in enumerate(file_paths):
        df = pd.read_csv(path)
        dfs.append(df)
        print(f"📄 Loaded {path} as df{i+1}")

    return dfs
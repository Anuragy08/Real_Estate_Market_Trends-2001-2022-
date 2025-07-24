# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 17:31:16 2025

@author: anura
"""

import pandas as pd

def count_columns(df):
    return df.shape[1]

def detect_column_types(df):
    print("Detected Column Data types")
    print(df.dtypes)
    print("-" * 40)
    
"""
Function: correct_dtypes(df)

Defines the main function resposible for:
- Analyzing the contents of each column
- Assigning the correct data type
- Returning a dictionary of colummn -> SQL data types(for MySQL)
"""
def correct_dtypes(df):
    
    corrected_types = {}

    
    for col in df.columns:
        print(f"Column's Name: {col}")
        series = df[col]
        datatype = df[col].dtype
        sample = series.dropna().head(5)
        parsed = pd.to_datetime(sample, errors='coerce')
        print(f"Column's present datatype: {datatype}")

    
        if pd.api.types.is_numeric_dtype(series):
            if series.dropna().apply(lambda x:float(x).is_integer()).all():
                corrected_types[col] = 'INT'
                print("Changed Type: INT")
            else:
                corrected_types[col] = 'FLOAT'
                print("Changed Type: FLOAT")
                
        elif parsed.notna().mean() > 0.6:
                print(f"'{col}' is likely a date column.")
                corrected_types[col] = 'date'
        else:
            corrected_types[col] = 'VARCHAR(255)'
            print("Changed Type: VARCHAR(255)")
    

    return df, corrected_types


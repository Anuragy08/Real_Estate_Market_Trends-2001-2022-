# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:29:06 2025

@author: anura
"""
import pandas as pd
import warnings

def convert_date_like_column(df):
    converted_cols = []
    
    for col in df.columns:
        if df[col].dtype == 'object':
            print(f"Running: {col}")
            sample = df[col].head(5)
            
            try:
                parsed = pd.to_datetime(sample, errors='coerce')
                if parsed.notna().sum() == 0:
                    print(f"{col} - Skip")
                    continue
            except:
                continue
            
            try:
                df[col] = pd.to_datetime(df[col], errors = 'coerce')
                df[col] = df[col].dt.strftime('%Y-%m-%d')
                print(f"{col} converted to MySQL compatible date-time format")
            except:
                print("Failed to convert")
                
                warnings.filterwarnings("ignore", category = UserWarning, module='pandas')
                
    return df
            
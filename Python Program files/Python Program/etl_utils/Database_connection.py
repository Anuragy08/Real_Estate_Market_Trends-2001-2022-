# -*- coding: utf-8 -*-
"""
Created on Mon Jul 14 12:51:07 2025

@author: anura
"""
from tqdm import tqdm
import pandas as pd
import mysql.connector 

def database_creator(sql_query, table_name, database_name, df):
    # MySQL Credentials
    host = 'localhost'
    user = 'root'
    password = 'V@nya'
    conn = None
    cursor = None

    try:
        #connect to MySQL Server
        conn = mysql.connector.connect(
            host = host,
            user = user,
            password = password,
            allow_local_infile = True
            )
        cursor = conn.cursor()
        
        #Create a new database
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
        print(f"Database {database_name} is successfully created or already exists")
        
        #Use newly created database
        cursor.execute(f"USE {database_name}")
        print(f"Database Switched! - {database_name}")
        
        cursor.execute(sql_query)
        print(f"Table {table_name} is successfully created in {database_name} database")
        
        df = df.where(pd.notnull(df),None)
        
        # Get column names and placeholders
        cols =",".join([f"`{col}`" for col in df.columns])
        col_clean = cols.strip().replace(" ", "_").lower()
        placeholders = ",".join(["%s"] * len(df.columns))
        insert_query = f"insert into `{table_name}` ({col_clean}) VALUES ({placeholders})"
        
        try:
            for row in tqdm(df.itertuples(index = False, name = None),
                            total = len(df), desc="Uploading"):
                cursor.execute(insert_query, row)
            conn.commit()
            print(f"Data uploaded to {table_name} successfully")
        except Exception as e:
            print("Error during upload", e)
            
    
    except mysql.connector.Error as err:
        print(err)

    finally:
        if conn:
            if cursor:
                cursor.close()
                conn.close()
                print("MySQL connection closed.")

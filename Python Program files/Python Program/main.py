import pandas as pd  
import os
from etl_utils.dateconversion import convert_date_like_column
from etl_utils.splitting import split_by_column_group
from etl_utils.read_dfs import read_split_files
from etl_utils.datatype_utils import correct_dtypes
from etl_utils.sql_generator import generate_create_table_sql
from etl_utils.Database_connection import database_creator
import warnings

# -------- USER CONFIGURATION --------
INPUT_FILE = "C:/Users/anura/OneDrive/Desktop/Projects/Real Estate Data/Raw Data/Real_Estate(RAW).csv"
OUTPUT_DIR = "C:/Users/anura/OneDrive/Desktop/Projects/Real Estate Data/Split_files"
PROCESSED_OUTPUT_DIR = "C:/Users/anura/OneDrive/Desktop/Projects/Real Estate Data/Processed_files"
SQL_OUTPUT_DIR = "C:/Users/anura/OneDrive/Desktop/Projects/Real Estate Data/SQL_Queries"
MISSING_STRATEGY = "fill"       # 'drop' or 'fill'
FILL_VALUE = "Unknown"          # Used if strategy = 'fill'
common_key = "SN"

# ------------------------------------


database_name = "Real_Estate_Database"

def main():
    warnings.filterwarnings("ignore")
    print("📥 Loading raw data...")
    df_raw = pd.read_csv(INPUT_FILE)
    
    split_files = split_by_column_group(df_raw, common_key, OUTPUT_DIR, split_size = None)
    
    print("📖 Reading split files into DataFrames...")
    dfs = read_split_files(split_files)
    
    file_paths = []
    for i, df_dateconvert in enumerate(dfs): # ✅ Loops through a list of DataFrames (dfs), keeping track of index
        df_processed = convert_date_like_column(df_dateconvert) # ✅ Converts date-like columns in the current DataFrame
        file_path = os.path.join(PROCESSED_OUTPUT_DIR, f"df_processed_{i+1}.csv") # ✅ Builds output file path
        df_processed.to_csv(file_path, index = False) # ✅ Writes the processed DataFrame to CSV without the index
        print(f"Processed file named:{file_path}")
        file_paths.append(file_path)

    print("📖 Reading split files into DataFrames...")
    df_n = read_split_files(file_paths)
    
    file_paths_2 = []
    for i, df_new in enumerate(df_n):
        df_changed_DT, corrected_types = correct_dtypes(df_new)
        file_paths_2.append(df_changed_DT)
        sql_query = generate_create_table_sql(f"real_estate_table_{i}", corrected_types, if_not_exists=True)
        table_name = f"real_estate_table_{i}"
        sql_file_path = os.path.join(SQL_OUTPUT_DIR, f"Table_name_{i}.txt")
        with open(sql_file_path, "w") as f:
            f.write(sql_query)
            
        database_creator(sql_query, table_name, database_name, df_changed_DT) 
        
    

if __name__ == "__main__":
    main() 
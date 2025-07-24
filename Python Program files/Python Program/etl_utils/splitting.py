# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 17:32:54 2025

@author: anura
"""

"""
Function Definition
"""
def split_by_column_group(df, common_key, output_dir, split_size = None):
    """
    Create Output Folder
    """
    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    if common_key not in df.columns:
        raise ValueError(f"{common_key} not found in columns")

    other_cols = [col for col in df.columns if col != common_key]
    total_cols = len(other_cols)
    print(f"Total Columns: {total_cols}")

    if not split_size:
        split_count = 3 # Default to 3 parts
        avg = total_cols//split_count
        rem = total_cols%split_count
        split_sizes = [avg + (1 if rem else 0) for i in range(split_count)]
        print("Split sizes: {split_size}")
        
    file_paths = []
    start = 0
    for i, size in enumerate(split_sizes):
        end = start + size
        col_group = other_cols[start:end]
        sub_df = df[[common_key] + col_group]
        file_path = os.path.join(output_dir, f"split_part_{i+1}.csv")
        sub_df.to_csv(file_path, index = False)
        print(f"✅ Saved: {file_path}")
        file_paths.append(file_path)
        start = end

    return file_paths  # Return the paths
    
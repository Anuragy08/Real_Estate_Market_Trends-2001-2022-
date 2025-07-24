# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 17:33:16 2025

@author: anura
"""

def generate_create_table_sql(table_name, column_types, if_not_exists=True):
    """
    Generates a MySQL CREATE TABLE script from column type mapping.

    Args:
        table_name (str): Name of the SQL table to create.
        column_types (dict): Dictionary of column names and their SQL datatypes.
        if_not_exists (bool): Add 'IF NOT EXISTS' clause. Default is True.

    Returns:
        str: CREATE TABLE SQL statement.
    """

    # Sanitize table name (optional improvement)
    table_name = table_name.strip().replace(" ", "_").lower()

    # Start query
    if if_not_exists:
        sql = f"CREATE TABLE IF NOT EXISTS `{table_name}` (\n"
    else:
        sql = f"CREATE TABLE `{table_name}` (\n"

    # Add column definitions
    col_defs = []
    for col, dtype in column_types.items():
        col_clean = col.strip().replace(" ", "_").lower()
        col_defs.append(f"  `{col_clean}` {dtype}")

    sql += ",\n".join(col_defs)
    sql += "\n);"

    return sql


def save_sql_to_file(sql_code, filename):
    """
    Saves the generated SQL code to a .sql file.

    Args:
        sql_code (str): SQL CREATE TABLE statement
        filename (str): Destination path (e.g. 'output/schema.sql')
    """
    with open(filename, "w") as file:
        file.write(sql_code)
    print(f"✅ SQL schema saved to: {filename}")

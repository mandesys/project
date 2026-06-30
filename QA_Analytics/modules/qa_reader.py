"""
==========================================================
QA Analytics Workbench
Module : qa_reader.py
Version : 1.0

Description
-----------
Read Excel file and validate dataset.

Author : NG Suyasa
==========================================================
"""

import pandas as pd


# ==========================================================
# READ EXCEL
# ==========================================================

def read_excel(file):
    """
    Read Excel file.

    Parameters
    ----------
    file : str or UploadedFile

    Returns
    -------
    pandas.DataFrame
    """

    try:

        df = pd.read_excel(file)

        return df

    except Exception as e:

        raise Exception(f"Cannot read Excel file.\n{e}")


# ==========================================================
# VALIDATE DATAFRAME
# ==========================================================

def validate_dataframe(df):
    """
    Validate dataframe.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    bool
    """

    if df is None:

        raise ValueError("DataFrame is None.")

    if df.empty:

        raise ValueError("Excel contains no data.")

    return True


# ==========================================================
# GET NUMERIC COLUMNS
# ==========================================================

def get_numeric_columns(df):
    """
    Return numeric columns.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    list
    """

    numeric_cols = list(
        df.select_dtypes(include="number").columns
    )

    return numeric_cols


# ==========================================================
# DATASET INFORMATION
# ==========================================================

def dataset_info(df):
    """
    Return dataset information.

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    dict
    """

    info = {

        "Rows": len(df),

        "Columns": len(df.columns),

        "ColumnNames": list(df.columns),

        "NumericColumns": get_numeric_columns(df),

        "MissingValues": df.isnull().sum().to_dict()

    }

    return info


# ==========================================================
# DATA PREVIEW
# ==========================================================

def preview(df, n=10):
    """
    Return first n rows.

    Parameters
    ----------
    df : pandas.DataFrame

    n : int

    Returns
    -------
    pandas.DataFrame
    """

    return df.head(n)


# ==========================================================
# CHECK COLUMN EXIST
# ==========================================================

def check_column(df, column):
    """
    Check whether selected column exists.

    Parameters
    ----------
    df : pandas.DataFrame

    column : str

    Returns
    -------
    bool
    """

    if column not in df.columns:

        raise ValueError(

            f"Column '{column}' not found."

        )

    return True


# ==========================================================
# GET SERIES
# ==========================================================

def get_series(df, column):
    """
    Return selected numeric column.

    Parameters
    ----------
    df : pandas.DataFrame

    column : str

    Returns
    -------
    pandas.Series
    """

    check_column(df, column)

    return df[column].dropna()


def get_numeric_columns(df):
    """
    Return semua kolom numerik.
    """

    return df.select_dtypes(include="number").columns.tolist()

# ==========================================================
# PRINT DATASET INFO
# ==========================================================

def print_dataset_info(df):
    """
    Print dataset information.
    """

    info = dataset_info(df)

    print("=" * 60)

    print("QA ANALYTICS DATASET")

    print("=" * 60)

    print(f"Rows           : {info['Rows']}")

    print(f"Columns        : {info['Columns']}")

    print()

    print("Column List")

    print("-" * 60)

    for c in info["ColumnNames"]:

        print(c)

    print()

    print("Numeric Columns")

    print("-" * 60)

    for c in info["NumericColumns"]:

        print(c)

    print()

    print("Missing Values")

    print("-" * 60)

    for c, v in info["MissingValues"].items():

        print(f"{c:25s} : {v}")

    print("=" * 60)
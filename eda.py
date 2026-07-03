import pandas as pd


def load_data(file):
    """
    Load CSV or Excel file
    """
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    return df


def dataset_summary(df):
    """
    Return dataset summary
    """
    summary = {}

    summary["Rows"] = df.shape[0]
    summary["Columns"] = df.shape[1]
    summary["Column Names"] = list(df.columns)

    summary["Data Types"] = df.dtypes.astype(str)

    summary["Missing Values"] = df.isnull().sum()

    summary["Duplicate Rows"] = df.duplicated().sum()

    summary["Statistics"] = df.describe(include="all")

    return summary

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df = df.copy()
    df.drop(['customerID'], axis=1, inplace=True)
    df.replace(" ", pd.NA, inplace=True)
    df.dropna(inplace=True)
    for col in df.select_dtypes(include='object'):
        if df[col].nunique() <= 2:
            df[col] = LabelEncoder().fit_transform(df[col])
        else:
            df = pd.get_dummies(df, columns=[col], drop_first=True)
    return df

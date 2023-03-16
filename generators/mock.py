import pandas as pd


def copycat(df: pd.DataFrame, num_samples: int) -> pd.DataFrame:
    """
    Generate mock dataframe.

    :param df: the original dataframe
    :param num_samples: the number of samples to generate
    :return: the mock dataframe
    """

    df_copy = df.sample(n=num_samples, replace=True)

    return df_copy


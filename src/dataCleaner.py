import pandas as pd

class DataCleaner:
    """Class for cleaning and preprocessing data.
    
    This class provides methods to clean raw datasets by removing missing values,
    duplicate rows, and other data quality issues.
    """

    def __init__(self, df: pd.DataFrame):
        """Initialize the DataCleaner with a DataFrame.
        
        Args:
            df (pd.DataFrame): The raw dataset to be cleaned.
        """
        self.df = df

    def clean_data(self) -> pd.DataFrame:
        """Remove rows with missing values and duplicate rows.

        Returns:
            pd.DataFrame: Cleaned DataFrame with no missing values or duplicates.
        """
        
        self.df.drop_duplicates(inplace=True)
        return self.df
    
    def convert_to_lowercase(self,) -> pd.DataFrame:
        """"Set the dataframe content to a lowercase letters.

        Returns:
             pd.DataFarame: with lowercase letters .
        """

        self.df = self.df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        return self.df
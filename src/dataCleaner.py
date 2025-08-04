import pandas as pd
import string

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

    def return_required_columns(self,required_columns : list) -> pd.DataFrame:
        """Remove columns that is not important to.

        Returns:
            pd.DataFrame: Cleaned DataFrame with only the required columns.
        """
        self.df = self.df[required_columns]
        return self.df
    
    def remove_punctuation(self, column_name: str) -> pd.DataFrame:
        """Remove punctuation from a specific column in the DataFrame.
        
        Args:
            column_name (str): The name of the column to remove punctuation from.
            
        Returns:
            pd.DataFrame: DataFrame with punctuation removed from the specified column.
        """
        translator = str.maketrans('', '', string.punctuation)
        self.df[column_name] = self.df[column_name].apply(lambda x: x.translate(translator) if isinstance(x, str) else x)
        return self.df

    def convert_to_lowercase(self,) -> pd.DataFrame:
        """"Set the dataframe content to a lowercase letters.

        Returns:
             pd.DataFrame: with lowercase letters .
        """

        self.df = self.df.applymap(lambda x: x.lower() if isinstance(x, str) else x)
        return self.df
    
    def remove_none_classify_raws(self) -> pd.DataFrame:
        """Remove rows that contain None or NaN values in classification columns.
        
        Returns:
            pd.DataFrame: DataFrame with rows containing None/NaN values removed.
        """
        self.df = self.df.dropna()
        return self.df
        

    

df = pd.read_csv(r"C:/Users/brdwn/Desktop/my_projects/Python/AppsProjects/HateFilter/Data/tweets_dataset.csv")
dd = DataCleaner(df)
x = dd.return_required_columns(["Text","Biased"])
print(x.head(15))


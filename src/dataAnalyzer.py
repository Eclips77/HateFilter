import pandas as pd


class DataAnalyzer:
    """Class for analyzing and processing data.
    
    This class provides methods to analyze  datasets ,
    and return some statistics about the current data.
    """

    def __init__(self, df: pd.DataFrame,categoryColumn : str):
        """Initialize the DataAnalyzer with a DataFrame.
        
        Args:
            df (pd.DataFrame): The raw dataset to be analyzed.
        """
        self.df = df
        self.category = categoryColumn
        
    
    def get_tweet_counts(self) -> dict:
        """Get the count of tweets by category.

        Returns:
            dict: A dictionary with categories as keys and their respective tweet counts as values.
        """
        if self.category not in self.df.columns:
            raise ValueError(f"Column '{self.category}' does not exist in the DataFrame.")
        
        tweets_count =  self.df[self.category].value_counts().to_dict()
        return {'tweets_count':tweets_count}
        

    def calculate_average_tweet_length(self,column : str) -> dict:
        """Calculate the average length of tweets in the dataset.

        Returns:
            dict: A dictionary with the average tweet length.
        """
        if column not in self.df.columns:
            raise ValueError(f"Column '{column}' does not exist in the DataFrame.")
        
        if self.category not in self.df.columns:
            raise ValueError(f"Column '{self.category}' does not exist in the DataFrame.")
        
        avg_length = self.df[column].apply(len).mean()
        avg_length_by_category = self.df.groupby(self.category)[column].apply(lambda x: x.apply(len).mean()).reset_index()
        return {'average_tweet_length': avg_length,'average_length_by_category':avg_length_by_category}

    

    # def calculate_the_longest_tweets(self) -> dict:


def longest_text_by_category(df, category_col, text_col):
    longest_text = df.groupby(category_col)[text_col].agg(
        longest_text=('Text', lambda x: x.loc[x.str.len().idxmax()]),
        overall_length=('Text', lambda x: x.str.len().max())
    ).reset_index()
    
    return longest_text.to_dict(orient='records')


df = pd.read_csv(r"C:/Users/brdwn/Desktop/my_projects/Python/AppsProjects/HateFilter/Data/tweets_dataset.csv")

x = longest_text_by_category(df,"Biased","Text")
print(x)


# data = DataAnalyzer(df)
# print(data.get_tweet_counts("Biased"))

# x = data.calculate_average_tweet_length("Text","Biased")
# print(x)

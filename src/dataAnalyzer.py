import pandas as pd
from collections import Counter


class DataAnalyzer:
    """Class for analyzing and processing data.
    
    This class provides methods to analyze  datasets ,
    and return some statistics about the current data.
    """

    def __init__(self, df: pd.DataFrame,categoryColumn : str,tweet_text_column: str):
        """Initialize the DataAnalyzer with a DataFrame.
        
        Args:
            df (pd.DataFrame): The raw dataset to be analyzed.
        """
        self.df = df
        self.category = categoryColumn
        self.content_column = tweet_text_column
        
    def get_tweet_counts(self) -> dict:
        """Get the count of tweets by category.

        Returns:
            dict: A dictionary with categories as keys and their respective tweet counts as values.
        """
        if self.category not in self.df.columns:
            raise ValueError(f"Column '{self.category}' does not exist in the DataFrame.")
        
        tweets_count =  self.df[self.category].value_counts().to_dict()
        return {'tweets_count':tweets_count}
        
    def calculate_average_tweet_length(self) -> dict:
        """Calculate the average length of tweets in the dataset.

        Returns:
            dict: A dictionary with the average tweet length.
        """
        if self.content_column not in self.df.columns:
            raise ValueError(f"Column '{self.content_column}' does not exist in the DataFrame.")
        
        if self.category not in self.df.columns:
            raise ValueError(f"Column '{self.category}' does not exist in the DataFrame.")
        
        avg_length = self.df[self.content_column].apply(len).mean()
        avg_length_by_category = self.df.groupby(self.category)[self.content_column].apply(lambda x: x.apply(len).mean()).reset_index()
        return {'average_tweet_length': avg_length,'average_length_by_category':avg_length_by_category}

    def get_3longest_tweets(self) -> dict:
        """Returns a dictionary containing the three longest tweets based on the length of their content.
        The method calculates the length of each tweet's content, sorts the DataFrame in descending order
        by content length, and retrieves the top three longest tweets.

        Returns:
            dict: A dictionary where the keys are the indices of the tweets and the values are the tweet contents.
        """
        sorted_df = self.df.assign(content_length=self.df[self.content_column].str.len()).sort_values(by='content_length', ascending=False)
        return sorted_df[self.content_column].head(3).to_dict()
        
    def get_most_common_words(self,top_n=10) -> dict:
        """"Returns a dictionary containing the ten most common words in the tweets column.
        This method concatenates all the tweets, splits them into words, counts their occurrences,
        and returns the top N most common words.
        Args:
            top_n (int): The number of most common words to return. Default is 10.

        

        """
    
        all_words = ' '.join(self.df[self.content_column].dropna())
        word_counts = Counter(all_words.split())
        return dict(word_counts.most_common(top_n))

    def get_



df = pd.read_csv(r"C:/Users/brdwn/Desktop/my_projects/Python/AppsProjects/HateFilter/Data/tweets_dataset.csv")

data = DataAnalyzer(df, "Biased", "Text")
x = data.get_most_common_words()
print(x)


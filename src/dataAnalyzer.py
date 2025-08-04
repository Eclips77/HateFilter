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
        self.message_column = tweet_text_column
        
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
        if self.message_column not in self.df or self.category not in self.df:
            raise ValueError("Missing required columns.")

        word_count = lambda text: len(str(text).split())
        self.df["word_count"] = self.df[self.message_column].apply(word_count)

        return {
            'average_tweet_word_count': self.df["word_count"].mean(),
            'average_word_count_by_category': self.df.groupby(self.category)["word_count"].mean().reset_index()
        }

    def get_3longest_tweets(self) -> dict:
        """Returns a dictionary containing the three longest tweets based on the length of their content.
        The method calculates the length of each tweet's content, sorts the DataFrame in descending order
        by content length, and retrieves the top three longest tweets.

        Returns:
            dict: A dictionary where the keys are the indices of the tweets and the values are the tweet contents.
        """
        sorted_df = self.df.sort_values(by=self.message_column, key=lambda x: x.str.len(), ascending=False)
        return sorted_df[self.message_column].head(3).to_dict()
        
    def get_most_common_words(self,top_n=10) -> dict:
        """"Returns a dictionary containing the ten most common words in the tweets column.
        This method concatenates all the tweets, splits them into words, counts their occurrences,
        and returns the top N most common words.
        Args:
            top_n (int): The number of most common words to return. Default is 10.

        

        """
    
        all_words = ' '.join(self.df[self.message_column].dropna())
        word_counts = Counter(all_words.split())
        return dict(word_counts.most_common(top_n))

    def count_capital_words(self) -> dict:
        """Count capital words by category.
        
        Returns:
            dict: Dictionary with category as key and capital word count as value.
        """
        capital_counts = self.df.groupby(self.category)[self.message_column].apply(
            lambda x: x.str.findall(r'\b[A-Z]+\b').str.len().sum()
        )
        return capital_counts.to_dict()

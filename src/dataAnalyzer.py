import pandas as pd


class DataAnalyzer:
    """Class for analyzing and processing data.
    
    This class provides methods to analyze  datasets ,
    and return some statistics about the current data.
    """

    def __init__(self, df: pd.DataFrame):
        """Initialize the DataAnalyzer with a DataFrame.
        
        Args:
            df (pd.DataFrame): The raw dataset to be analyzed.
        """
        self.df = df
        
      


# c = df[category].value_counts().to_dict
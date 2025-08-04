from src.dataAnalyzer import DataAnalyzer
from src.dataCleaner import DataCleaner
from src.dataLoader import DataLoader
import pandas as pd
import json
import os
from datetime import datetime


class AppManager:
    def __init__(self):
        self.data_path = "Data/tweets_dataset.csv"
        self.results_dir = "results"
        self.cleaned_data_path = os.path.join(self.results_dir, "cleaned_tweets_data.csv")
        self.statistics_path = os.path.join(self.results_dir, "data_statistics.json")
        self.raw_data = None
        self.cleaned_data = None
        self.statistics = {}
        
        if not os.path.exists(self.results_dir):
            os.makedirs(self.results_dir)
    
    def run_analysis(self):
        """Main method that runs the complete analysis pipeline."""        
        self.load_data()
        
        self.analyze_data()
        
        self.save_statistics()
        
        self.clean_data()
        
        self.save_cleaned_data()
        
        # return self.statistics
    
    def load_data(self):
        """Load the raw data from CSV file."""
        try:
            self.raw_data = DataLoader.load_csv(self.data_path)
            print("Data loaded successfully")
        except Exception as e:
            print(f"Error loading data: {e}")
            raise
    
    def clean_data(self):
        """Clean the raw data using DataCleaner."""
        if self.raw_data is None:
            raise ValueError("No data loaded. Call load_data() first.")
        
        cleaner = DataCleaner(self.raw_data.copy())
        
        required_columns = ['Text','Biased']
        cleaner.return_required_columns(required_columns)
        
        cleaner.remove_punctuation('Text')
        
        cleaner.convert_to_lowercase()
        
        self.cleaned_data = cleaner.df
        print("Data cleaned successfully")
    
    def save_cleaned_data(self):
        """Save the cleaned data to CSV file."""
        if self.cleaned_data is None:
            raise ValueError("No cleaned data available. Call clean_data() first.")
        
        self.cleaned_data.to_csv(self.cleaned_data_path, index=False)
        print("Cleaned data saved successfully")
    
    def analyze_data(self):
        """Analyze the raw data and generate statistics."""
        if self.raw_data is None:
            raise ValueError("No data loaded. Call load_data() first.")
        
        analyzer = DataAnalyzer(self.raw_data, 'Biased', 'Text')
        
        self.statistics = {
            'analysis_timestamp': datetime.now().isoformat(),
            'dataset_info': {
                'total_tweets': len(self.raw_data),
                'total_columns': len(self.raw_data.columns),
                'column_names': list(self.raw_data.columns)
            }
        }
        
        tweet_counts = analyzer.get_tweet_counts()
        self.statistics.update(tweet_counts)
        
        avg_length = analyzer.calculate_average_tweet_length()
        self.statistics.update(avg_length)
        
        if 'average_word_count_by_category' in self.statistics:
            self.statistics['average_word_count_by_category'] = self.statistics['average_word_count_by_category'].to_dict('records')
        
        longest_tweets = analyzer.get_3longest_tweets()
        self.statistics['longest_tweets'] = longest_tweets
        
        common_words = analyzer.get_most_common_words(top_n=10)
        self.statistics['most_common_words'] = common_words
        
        capital_words = analyzer.count_capital_words()
        self.statistics['capital_words_by_category'] = capital_words
        
        print("Statistics analysis completed successfully")
    
    def save_statistics(self):
        """Save the statistics to JSON file."""
        if not self.statistics:
            raise ValueError("No statistics available. Call analyze_data() first.")
        
        with open(self.statistics_path, 'w', encoding='utf-8') as f:
            json.dump(self.statistics, f, indent=2, ensure_ascii=False)
        
        print("Statistics saved successfully")
    
   
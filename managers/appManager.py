import pandas as ps
from src.dataAnalyzer import DataAnalyzer
from src.dataCleaner import DataCleaner
from src.dataLoader import DataLoader




class AppManager:
    def __init__(self):
        self.data_analyzer = DataAnalyzer()
        self.data_cleaner = DataCleaner()

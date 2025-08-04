from managers.appManager import AppManager

def main():
    """Main function to run the complete data analysis pipeline."""
    manager = AppManager()
    manager.run_analysis()
    
if __name__ == "__main__":
    main()
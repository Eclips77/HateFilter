# HateFilter

**HateFilter** is a machine learning tool that filters and classifies text content (such as tweets) as antisemitic hate speech or not. It loads a dataset of texts, cleans the data (removing punctuation, lowercasing, etc.), and provides analysis of the content. The system generates useful statistics about the dataset to help understand the distribution and characteristics of the hate speech content.

## Usage

1. **Installation:** Ensure you have **Python 3** and install the required library  use pip install -r requirements.txt.
2. **Prepare the Data:** Provide a CSV file with your text data. By default, the program expects a file at `Data/tweets_dataset.csv` containing at least a **Text** column (the text content) and a **Biased** column (the label indicating whether each text is antisemitic or not). You can use your own dataset by placing it in this path or updating the file path in the code.
3. **Run the Analysis:** Execute the main script to run the pipeline:

   ```cli
   python main.py
   ```

   This will load the dataset, run the cleaning steps, and perform the analysis. The output files will be saved in the **`results/`** directory.

## Outputs

After running the program, you will find two output files in the `results/` folder:

* **Cleaned Data (CSV):** A cleaned version of the dataset (`cleaned_tweets_data.csv`) containing just the relevant text and label columns. All text is lowercased and stripped of punctuation for consistency.
* **Statistics (JSON):** A JSON file (`data_statistics.json`) with a summary of analysis results. This includes:

  * Total number of texts and columns in the dataset.
  * Count of texts by category how many are antisemitic vs not.
  * Average words per text overall and broken down by category.
  * The three longest texts in the dataset by character length.
  * The top 10 most common words in the text content.
  * The count of all-uppercase words in texts, grouped by category.

Using these outputs, you can understand the composition of your dataset and identify the prevalence and characteristics of hateful content. This core functionality helps in analyzing hate speech in text and preparing the data for further modeling or filtering efforts.

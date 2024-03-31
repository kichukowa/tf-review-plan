import pandas as pd
import matplotlib.pyplot as plt
from google.cloud import storage

# Your Google Cloud Storage bucket name
BUCKET_NAME = 'temp-example-storage-tf'

def load_data(file):
    """Load data from a local CSV file."""
    return pd.read_csv(file)

def analyze_data(df):
    """Perform data analysis and generate plots."""
    # Calculate summary statistics
    summary_stats = df['SalesAmount'].describe()

    # Generate a histogram of the SalesAmount column
    plt.figure()
    df['SalesAmount'].hist(bins=10)
    plt.title('Sales Amount Distribution')
    plt.xlabel('Sales Amount')
    plt.ylabel('Frequency')
    plt.savefig('plot.png')  # Save the plot as a PNG file

    return summary_stats

def save_to_gcs(file_name, bucket_name):
    """Save files to Google Cloud Storage."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_filename(file_name)

def main():
    # Load the dataset
    df = load_data('python/example_data.csv')

    # Perform the analysis
    summary_stats = analyze_data(df)

    # Save the summary statistics to a CSV file
    summary_stats.to_csv('summary_stats.csv')

    # Upload the analysis results to Google Cloud Storage
    save_to_gcs('summary_stats.csv', BUCKET_NAME)
    save_to_gcs('plot.png', BUCKET_NAME)
    print("Analysis results uploaded to Google Cloud Storage.")

if __name__ == '__main__':
    main()
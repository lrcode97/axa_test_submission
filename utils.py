import logging
import numpy as np
import pandas as pd
from pathlib import Path
from kaggle.api.kaggle_api_extended import KaggleApi

ISKAGGLE = False  # Set this to True if running in a Kaggle environment

class DepressionDataProcessor:
    def __init__(self, dataset="anthonytherrien/depression-dataset"):
        self.is_kaggle = ISKAGGLE
        self.dataset = dataset
        self.path = self.set_path()

    def set_path(self):
        """Determine dataset path based on execution environment."""
        if self.is_kaggle:
            return f"/kaggle/input/{self.dataset.split('/')[-1]}"
        return f"./datasets/{self.dataset.split('/')[-1]}"

    def download_and_extract(self):
        """Download and extract dataset if running locally."""
        if not self.is_kaggle:
            dataset_path = Path(self.path)
            print(dataset_path)
            if not dataset_path.exists():
                logging.info("Downloading dataset using Kaggle API...")
                api = KaggleApi()
                api.authenticate()

                # Create local dataset directory
                dataset_path.parent.mkdir(parents=True, exist_ok=True)

                # Download dataset
                api.dataset_download_files(self.dataset, path=dataset_path.parent, unzip=True)
                logging.info("Dataset downloaded and extracted successfully.")

    def load_data(self, filename):
        """Load a CSV file from the dataset directory."""
        file_path = Path(self.path).parent / filename
        if file_path.exists():
            return pd.read_csv(file_path)
        raise FileNotFoundError(f"File {filename} not found in {self.path}")

    def preprocess(self, df):
        """Preprocess dataset: handle missing values, convert dates, and concatenate."""

        # Create income buckets keeping scale in place
        df['Income Bucket'] = pd.cut(df['Income'], 
                         bins=[0, 20000, 40000, 60000, 80000, 100000, np.inf], 
                         labels=['0-20k', '20-40k', '40-60k', '60-80k', '80-100k', '100k+']).astype(str)

        df['Income Bucket Employment Status'] = df['Income Bucket'].astype(str) + df['Employment Status']

        # Create age buckets with more meaningful ranges
        df['Age Bucket'] = pd.cut(df['Age'], bins=[0, 12, 18, 25, 35, 45, 55, 65, np.inf], labels=['Child', 'Teen', 'Young Adult', 'Adult', 'Middle Age', 'Senior', 'Elderly', 'Very Elderly']).astype(str)
        
        #turn number opf children into a string
        df['Number of Children'] = df['Number of Children'].astype(str)
        
        # Split name into first and last name
        df[['First Name', 'Last Name']] = df['Name'].str.split(' ', n=1, expand=True)

        # Create attended university column
        df['Attended University'] = df['Education Level'].apply(lambda x: 'yes' if 'degree' in x.lower() else 'no')

        # Drop unnecessary columns
        df.drop(columns=['First Name', 'Name'], inplace=True)

        # Convert object types to categorical
        for col in df.select_dtypes(include='object').columns:
            df[col] = df[col].astype('category')

        # Convert 'History of Mental Illness' to 1 for 'Yes' and 0 for 'No'
        df['History of Mental Illness'] = df['History of Mental Illness'].apply(lambda x: 1 if x == 'Yes' else 0)

        return df
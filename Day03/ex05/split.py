import sys
import pandas as pd
from sklearn.model_selection import train_test_split


def main():
    """split Train_knight.csv"""
    if len(sys.argv) != 2:
        print("Usage: python3 split.py Train_knight.csv")
        sys.exit(1)
    input_file = sys.argv[1]
    try:
        df = pd.read_csv(input_file)
    except FileNotFoundError:
        print(f"File {input_file} not found.")
        sys.exit(1)

    # test_size=0.2 means we want to separate 20% of the datasets for Validation 
    train_df, validation_df = train_test_split(df, test_size=0.2, random_state=42)
    train_df.to_csv('Training_knight.csv', index=False)
    validation_df.to_csv('Validation_knight.csv', index=False)

    print(f"Dataset split completed: 80% training, 20% validation.")
    print("Files created: Training_knight.csv, Validation_knight.csv")


if __name__ == "__main__":
    main()

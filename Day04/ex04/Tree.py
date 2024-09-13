import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score


def load_file(path: str):
    """load a data file"""

    try:
        assert isinstance(path, str), "your path is not valid."
        assert os.path.exists(path), "your file doesn't exist."
        assert os.path.isfile(path), "your 'file' is not a file."
        assert path.lower().endswith(".csv"), "file format is not .csv."
        data = pd.read_csv(path)
        return data
    except AssertionError as msg:
        print(f"{msg.__class__.__name__}: {msg}")
        return None


def main():
    """create Tree.txt for Jedi and Sith predictions"""

    if len(sys.argv) != 3 or "Train_knight.csv" not in sys.argv[1] or "Test_knight.csv" not in sys.argv[2]:
        print("Usage: python3 Tree.py /path/to/Train_knight.csv /path/to/Test_knight.csv")
        sys.exit(1)
    df_train = load_file(sys.argv[1])
    df_test = load_file(sys.argv[2])

    x = df_train.drop(columns="knight")
    y = df_train["knight"]
    x_train, x_val, y_train, y_val = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    model = DecisionTreeClassifier(random_state=42)
    model.fit(x_train, y_train)
    predicted_val = model.predict(x_val)
    accuracy = accuracy_score(predicted_val, y_val)
    print(f"accuracy: {accuracy}")
    print(
        f"f1_score: {f1_score(y_val, predicted_val, average='macro')}"
    )

    predicted_test = model.predict(df_test)
    with open("Tree.txt", "w") as output:
        for item in predicted_test:
            output.write(item + "\n")

    plt.figure(figsize=(10, 7))
    plot_tree(
        model,
        feature_names=df_test.columns,
        class_names=["Jedi", "Sith"],
        filled=True,
    )
    plt.show()


if __name__ == "__main__":
    main()

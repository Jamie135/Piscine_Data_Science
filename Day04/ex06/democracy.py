import sys
import os
import pandas as pd
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score
from sklearn.preprocessing import StandardScaler


def load(path: str):
    """load a data"""
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
    """create Voting.txt for Jedi and Sith predictions"""

    if len(sys.argv) != 3 or "Train_knight.csv" not in sys.argv[1] or "Test_knight.csv" not in sys.argv[2]:
        print("Usage: python3 Tree.py /path/to/Train_knight.csv /path/to/Test_knight.csv")
        sys.exit(1)
    df_train = load(sys.argv[1])
    df_test = load(sys.argv[2])

    scaler = StandardScaler()
    x = df_train.drop(columns=["knight"])
    x = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)
    y = df_train["knight"]
    x_train, x_valid, y_train, y_valid = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    model1 = DecisionTreeClassifier(random_state=42)
    model2 = KNeighborsClassifier(n_neighbors=10)
    model3 = LogisticRegression(max_iter=1000, random_state=42)

    voting = VotingClassifier(
        estimators=[("dt", model1), ("knn", model2), ("lg", model3)],
        voting="hard",
    )
    voting.fit(x_train, y_train)
    predicted_val = voting.predict(x_valid)
    accuracy = accuracy_score(y_valid, predicted_val)
    print(f"Accuracy: {accuracy}")
    print(
        f"F1_score: {f1_score(y_valid, predicted_val, average='macro')}"
    )

    df_test = pd.DataFrame(scaler.fit_transform(df_test), columns=df_test.columns)
    predicted_test = voting.predict(df_test)
    with open("Voting.txt", "w") as output:
        for item in predicted_test:
            output.write(item + "\n")


if __name__ == "__main__":
    main()

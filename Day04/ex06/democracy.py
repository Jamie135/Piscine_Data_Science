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
    """load a data file using pandas library"""
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
    train_knight = load(sys.argv[1])
    test_knight = load(sys.argv[2])
    if train_knight is not None and test_knight is not None:
        x = train_knight.drop(
            columns=[
                "knight",
                "Prescience",
                "Push",
                "Deflection",
                "Survival",
                "Midi-chlorien",
                "Grasping",
                "Pull",
                "Awareness",
                "Repulse",
                "Attunement",
                "Empowered",
                "Dexterity",
                "Delay",
                "Slash",
                "Sprint",
                "Sensitivity",
                "Stims",
                "Strength",
                "Recovery",
                "Hability",
            ]
        )
        scaler = StandardScaler()
        x = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)
        y = train_knight["knight"]
        x_train, x_val, y_train, y_val = train_test_split(
            x, y, test_size=0.2, random_state=42
        )

        model1 = DecisionTreeClassifier(random_state=13)
        model2 = KNeighborsClassifier(n_neighbors=9)
        model3 = LogisticRegression(max_iter=1000, random_state=123)

        voting = VotingClassifier(
            estimators=[("dt", model1), ("knn", model2), ("lg", model3)],
            voting="hard",
        )
        voting.fit(x_train, y_train)
        predicted_val = voting.predict(x_val)
        accuracy = accuracy_score(y_val, predicted_val)
        print(f"Accuracy: {accuracy}")
        print(
            f"F1_score: {round(f1_score(y_val, predicted_val, average='macro'), 4)}"
        )

        x = test_knight.drop(
            columns=[
                "Prescience",
                "Push",
                "Deflection",
                "Survival",
                "Midi-chlorien",
                "Grasping",
                "Pull",
                "Awareness",
                "Repulse",
                "Attunement",
                "Empowered",
                "Dexterity",
                "Delay",
                "Slash",
                "Sprint",
                "Sensitivity",
                "Stims",
                "Strength",
                "Recovery",
                "Hability",
            ]
        )
        test_knight = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)
        predicted_test = voting.predict(test_knight)
        with open("Voting.txt", "w") as output:
            for item in predicted_test:
                output.write(item + "\n")


if __name__ == "__main__":
    main()
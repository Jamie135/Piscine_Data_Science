import sys
import os
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


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
    """create KNN.txt for Jedi and Sith predictions"""

    if len(sys.argv) != 3 or "Train_knight.csv" not in sys.argv[1] or "Test_knight.csv" not in sys.argv[2]:
        print("Usage: python3 Tree.py /path/to/Train_knight.csv /path/to/Test_knight.csv")
        sys.exit(1)
    df_train = load(sys.argv[1])
    df_test = load(sys.argv[2])

    x = df_train.drop(
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
            "Agility",
        ]
    )
    scaler = StandardScaler()
    x = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)
    y = df_train["knight"]
    x_train, x_valid, y_train, y_valid = train_test_split(
        x, y, test_size=0.2, random_state=42
    )

    accuracies = []
    for k in range(1, 30):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(x_train, y_train)
        y_pred = model.predict(x_valid)
        accuracy = accuracy_score(y_valid, y_pred)
        precision = precision_score(y_valid, y_pred, average='macro')
        f1 = f1_score(y_valid, y_pred, average='macro')
        accuracies.append(accuracy_score(y_valid, y_pred))
        print(f"k={k}: Accuracy={accuracy:.2f}, Precision={precision:.2f}, f1_score={f1:.2f}")
    # model = KNeighborsClassifier(n_neighbors=10)
    # model.fit(x_train, y_train)
    # y_pred = model.predict(x_valid)
    # accuracy = accuracy_score(y_valid, y_pred)
    # print(f"Accuracy: {accuracy}")
    # print(
    #     f"F1_score: {f1_score(y_valid, y_pred, average='macro')}"
    # )

    x = df_test.drop(
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
            "Agility",
        ]
    )
    df_test = pd.DataFrame(scaler.fit_transform(x), columns=x.columns)
    predicted_test = model.predict(df_test)
    with open("KNN.txt", "w") as output:
        for item in predicted_test:
            output.write(item + "\n")

    plt.plot(accuracies)
    plt.xlabel("k values")
    plt.ylabel("accuracy")
    plt.yticks([i/1000 for i in range(920, 985, 5)])
    plt.show()


if __name__ == "__main__":
    main()
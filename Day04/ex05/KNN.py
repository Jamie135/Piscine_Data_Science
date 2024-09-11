import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, precision_score


def load_file(path: str):
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
    """create Tree.txt for Jedi and Sith predictions"""

    if len(sys.argv) != 3 or "Train_knight.csv" not in sys.argv[1] or "Test_knight.csv" not in sys.argv[2]:
        print("Usage: python3 Tree.py /path/to/Train_knight.csv /path/to/Test_knight.csv")
        sys.exit(1)
    df_train = load_file(sys.argv[1])
    df_test = load_file(sys.argv[2])

    x = df_train.drop(columns=["knight"])
    y = df_train["knight"]
    x_train, x_valid, y_train, y_valid = train_test_split(x, y, test_size=0.2, random_state=42)

    k_values = range(1, 30)
    accuracies = []
    precisions = []
    f1_scores = []

    for k in k_values:
        knn = KNeighborsClassifier(n_neighbors=k)
        knn.fit(x_train, y_train)
        y_pred = knn.predict(x_valid)
        
        accuracy = accuracy_score(y_valid, y_pred)
        precision = precision_score(y_valid, y_pred, average='macro')
        f1 = f1_score(y_valid, y_pred, average='macro')

        accuracies.append(accuracy)
        precisions.append(precision)
        f1_scores.append(f1)

        print(f"k={k}: Accuracy={accuracy:.2f}, Precision={precision:.2f}, f1_score={f1:.2f}")

    train_pred = knn.predict(df_test)
    with open("KNN.txt", "w") as file:
        for pred in train_pred:
            file.write(pred + "\n")

    plt.figure(figsize=(8, 6))
    plt.plot(k_values, accuracies)
    plt.xlabel('k value')
    plt.ylabel('accuracy')
    plt.yticks([i/1000 for i in range(920, 985, 5)])
    plt.show()  


if __name__ == "__main__":
    main()

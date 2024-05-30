import csv
from collections import Counter

def predict_class(k, user_input, data):
    len = [(sum((x - y) ** 2 for x, y in zip(user_input, features)) ** 0.5, label) for features, label in data]
    return Counter(label for _, label in sorted(len)[:k]).most_common(1)[0][0]

if __name__ == "__main__":
    k = 5
    with open("data.csv") as file:
        data = [(list(map(float, row[:-1])), row[-1]) for i, row in enumerate(csv.reader(file)) if i != 0]
    input_str = input("Enter sepal length, sepal width, petal length, petal width separated by commas: ")
    user_input = list(map(float, input_str.split(',')))
    print("Predicted class:", predict_class(k, user_input, data))

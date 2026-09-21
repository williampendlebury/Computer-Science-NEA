import numpy as np

x = np.array([
    [22, 25000],
    [25, 30000],
    [35, 45000],
    [42, 60000],
    [50, 35000]
])

y = np.array([
    [1],
    [1],
    [1],
    [0],
    [0]
])

def gini(labels):
    values, counts = np.unique(labels, return_counts=True)
    proportions = counts / len(labels)
    return 1 - np.sum(proportions ** 2)

print(gini(y))
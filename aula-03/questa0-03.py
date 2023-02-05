# Solução

import numpy as np

def locate_outliers(X):
    q3 = np.percentile(X, 75)
    q1 = np.percentile(X, 25)
    iqr = q3 - q1
    outliers = np.concatenate([(X[X < (iqr * 1.5 - q1)]), X[X > (iqr * 1.5 + q3)]])
    outliers_count = outliers.size
    is_outlier = np.isin(X, outliers)
    return is_outlier, outliers_count, outliers

X = np.random.rand(4,4)
print(X)
print("-----------------------------------------------")

is_outlier, outliers_count, outliers = locate_outliers(X)

print(is_outlier)
print(outliers_count)
print(outliers)
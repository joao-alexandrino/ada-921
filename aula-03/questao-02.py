# Solução

import numpy as np

def process_EEG_signal(X):
    X_mean = np.reshape(np.mean(X, axis = 1), (-1,1))
    return (X - X_mean)


# Solução alternativa

def process_EEG_signal_2(X):
    X_mean = np.split(np.mean(X, axis = 1), X.shape[0])
    return (X - X_mean)


X = np.random.randn(3,5)
# print(X.shape)
X_processado = process_EEG_signal(X)
# print(X_processado.shape)
# print((X_processado - X).sum())
print(X)
print("---------------------------------------------------------------")
print(X_processado)
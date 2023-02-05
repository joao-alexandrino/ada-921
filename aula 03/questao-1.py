# Solução

import numpy as np

y_prediction = np.array([1,2,3])
y_i = np.array([0,0,3])

def calculate_eqm(y_prediction, y_i):
    return (1/y_i.size) * ((y_prediction - y_i)**2).sum()

print(calculate_eqm(y_prediction,y_i))

# Solução alternativa

def calculate_eqm_2(y_prediction, y_i):
    return (1/len(y_prediction)) * sum((y_prediction - y_i)**2)

print(calculate_eqm_2(y_prediction,y_i))
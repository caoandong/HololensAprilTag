import numpy as np

def rescale(mag, vec):
    vec = np.array(vec)
    return mag * vec / np.linalg.norm(vec)

print(rescale(0.122, [-8, 10]))
print(rescale(0.101, [8, 7]))
print(rescale(0.0835, [-5.4, -7]))
print(rescale(0.1085, [5.4, -10]))
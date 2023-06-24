Import numpy as np

arr = np.array([[15, 27, 13], [49, 25, 62], [70, 81, 92]])
difference = np.diff(arr, axis=1)
print(difference)

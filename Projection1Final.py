import numpy as np

x = 28
arr = np.arange(784).reshape(x, x)
print(arr)

projection_1 = []

print("\n")

for i in range(28):
    projection_1.append(sum(arr[i]))

print(projection_1)
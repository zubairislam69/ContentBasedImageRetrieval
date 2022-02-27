import numpy as np
from itertools import islice

x = 28
arr = np.arange(784).reshape(x, x)
print(arr)

projection_3_initial = []
projection_3_final = []
split_by_length = []


print("\n")

for j in range(28):
    for i in range(x):
        projection_3_initial.append(arr[i][27-j])

for i in range (28):
    split_by_length.append(28)

inputt = iter(projection_3_initial)
output = [list(islice(inputt, elem))
          for elem in split_by_length]

for i in range(x):
    projection_3_final.append(sum(output[i]))

print(projection_3_final)


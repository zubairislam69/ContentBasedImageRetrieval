import numpy as np

x = 4

arr = np.arange(16).reshape(x, x)
print(arr)

# i want (8,13), (4,9,14), (0, 5, 10, 15), (1, 6, 11), (2, 7)

diagonal_array_1 = []
diagonal_array_2 = []
diagonal_array_3 = []
diagonal_array_4 = []
diagonal_array_5 = []
diagonal_array_mid = []

# get 52 variables to store each diagonal set of values, so they can be summed later,
# and all the variable sums can be added into a list,
# to make one projection

for i in range(x):
    diagonal_array = {i: ''}

sum = 0

# amount of diagonals on both sides of center diagonal is x-2
for i in range(x):  # for (int i = 0; i < 4; i++)
    diagonal_array_mid.append(arr[i][i])

    if i + (x - 2) < x:  # runs 2 times // starts from 1 above bottom diagonal
        # diagonal_array_1.append(arr[(x - 2) + i][i])
        sum += arr[(x - 2) + i][i]
        print(sum)
        diagonal_array_4.append(arr[i][i + 2])
        #
       # sum += diagonal_array_1[i]

    if i + (x - 3) < x: # if i + (28 - _) < 28
        diagonal_array_2.append(arr[(x - 3) + i][i])
        diagonal_array_3.append(arr[i][i + 1])


# def diagonal(diag):



    # if i + (x - 4) < x:                 # up to 27
    #
    # if i + (x - 5) < x:
    # if i + (x - 6) < x:
    # if i + (x - 7) < x:
    # if i + (x - 8) < x:
    # if i + (x - 9) < x:
    # if i + (x - 10) < x:

print(' 1 =', diagonal_array_1)
print(' 2 =', diagonal_array_2)
print(' 3 =', diagonal_array_mid)
print(sum)
print(' 4 =', diagonal_array_3)
print(' 5 =', diagonal_array_4)

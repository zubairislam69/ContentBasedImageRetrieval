import numpy as np
import seaborn as sns;

from itertools import islice

sns.set()

x = 28

arr = np.arange(784).reshape(x, x)
print(arr)

# ax = sns.heatmap(arr, annot=True, fmt="d")
#
# plt.show()

d = dict(enumerate(arr.flatten(), 1))

print(d)
print("\n")

n = 29

projection_2_top_initial = []
projection_2_top_final = []
split_by_length = []
split_by_length2 = []

for j in range(26):
    for i in range((27-j), ((x*x) - (725 - (29*j))), n):  # 29(28-3) want 3 to increment
        projection_2_top_initial.append(d.get(i))

for j in range(28):
    for i in range(28):
        projection_2_top_initial.append(arr[i][27-j])

for i in range(26):   # 2- 27
    split_by_length.append(i+2)
    split_by_length2.append(27-i)

inputt = iter(projection_2_top_initial)
output = [list(islice(inputt, elem))
          for elem in split_by_length]

for i in range(26):
    projection_2_top_final.append(sum(output[i]))

main_diagonal_initial = []
main_diagonal = []

# Top half end

sum1 = 0
for i in range(1, 800, n):  # start from 0 // GETS MAIN DIAGONAL FROM TOP LEFT TO BOTTOM RIGHT
    main_diagonal_initial.append(d.get(i))

main_diagonal.append(sum(main_diagonal_initial))

# Bottom half

projection_2_bottom_initial = []
projection_2_bottom_final = []

for j in range(26):
    for i in range((28 + (1+(28*j))), 784, n):  # 729
        projection_2_bottom_initial.append(d.get(i))

for j in range(28):
    for i in range(28):
        projection_2_bottom_initial.append(arr[i][27 - j])


inputt = iter(projection_2_bottom_initial)
output = [list(islice(inputt, elem))
    for elem in split_by_length2]

for i in range(26):
    projection_2_bottom_final.append(sum(output[i]))

projection_2 = []

projection_2.append(projection_2_top_final + main_diagonal + projection_2_bottom_final)

print("\nProjection 2")

print(projection_2)

# print(sum1)
#
# print(projection_2)
#
# proj_2_average = (round(sum(projection_2) / len(projection_2), 0))
#
# print(proj_2_average)
#
#
# def generate_c(p):
#     c = []
#     for item in p:
#         if item > proj_2_average:
#             c.append(1)
#         else:
#             c.append(0)
#     return c
#
#
# #
# #
# c2 = generate_c(projection_2)
#
# print('c2:', c2)

import numpy as np
import seaborn as sns;

from itertools import islice

sns.set()

x = 28

arr = np.arange(784).reshape(x, x)


d = dict(enumerate(arr.flatten(), 1))

n = 27

projection_4_top_initial = []
projection_4_top_final = []

projection_4_bottom_initial = []
projection_4_bottom_final = []

main_diagonal_initial_P4 = []
main_diagonal_P4 = []

split_by_length_top = []
split_by_length_bottom = []

for i in range(26):
    split_by_length_bottom.append(i + 2)
    split_by_length_top.append(27 - i)

for j in range(26):
    for i in range(756-(28*j), 800-j, n):  # bottom right up to mid diagonal
        projection_4_bottom_initial.append(d.get(i))

    for i in range(27-j, 730-(28*j), n):  # from mid diagonal to top left
        projection_4_top_initial.append(d.get(i))

for j in range(28):
    for i in range(28):
        projection_4_top_initial.append(arr[i][27 - j])  # Top Half Diagonals
        projection_4_bottom_initial.append(arr[i][27 - j])  # Bottom Half Diagonals


print("top init")
print(projection_4_top_initial)
print("bottom init")
print(projection_4_bottom_initial)


input_bottom_P4 = iter(projection_4_bottom_initial)
output_bottom_P4 = [list(islice(input_bottom_P4, elem))
                    for elem in split_by_length_bottom]

input_top_P4 = iter(projection_4_top_initial)
output_top_P4 = [list(islice(input_top_P4, elem))
                 for elem in split_by_length_top]

print("output top")
print(output_top_P4)
print("output bottom")
print(output_bottom_P4)

for i in range(26):
    projection_4_top_final.append(sum(output_top_P4[i]))
    projection_4_bottom_final.append(sum(output_bottom_P4[i]))

print("top final")
print(projection_4_top_final)

print("bottom final")
print(projection_4_bottom_final)

for i in range(28, 770, n):  # GETS MAIN DIAGONAL FROM TOP LEFT TO BOTTOM RIGHT
    main_diagonal_initial_P4.append(d.get(i))

main_diagonal_P4.append(sum(main_diagonal_initial_P4))

projection_4 = (projection_4_bottom_final + main_diagonal_P4 + projection_4_top_final)

print("\nProjection 4")
print(projection_4)



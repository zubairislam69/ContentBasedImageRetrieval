import numpy as np
import seaborn as sns;

from itertools import islice

sns.set()

x = 28

arr = np.arange(784).reshape(x, x)


d = dict(enumerate(arr.flatten(), 1))

n = 29

projection_2_top_initial = []
projection_2_top_final = []

projection_2_bottom_initial = []
projection_2_bottom_final = []

main_diagonal_initial = []
main_diagonal = []

split_by_length_top = []
split_by_length_bottom = []

for i in range(26):  # 2- 27
    split_by_length_top.append(i + 2)
    split_by_length_bottom.append(27 - i)

for j in range(26):
    for i in range((27 - j), (784 - (725 - (29 * j))), n):  #26, 88
        projection_2_top_initial.append(d.get(i))

    for i in range((28 + (1 + (28 * j))), 784, n):  # 729
        projection_2_bottom_initial.append(d.get(i))

for j in range(28):
    for i in range(28):
        projection_2_top_initial.append(arr[i][27 - j])  # Top Half Diagonals
        projection_2_bottom_initial.append(arr[i][27 - j])  # Bottom Half Diagonals

input_top = iter(projection_2_top_initial)
output_top = [list(islice(input_top, elem))
              for elem in split_by_length_top]

input_bottom = iter(projection_2_bottom_initial)
output_bottom = [list(islice(input_bottom, elem))
                 for elem in split_by_length_bottom]

for i in range(26):
    projection_2_top_final.append(sum(output_top[i]))
    projection_2_bottom_final.append(sum(output_bottom[i]))

for i in range(1, 800, n):  # GETS MAIN DIAGONAL FROM TOP LEFT TO BOTTOM RIGHT
    main_diagonal_initial.append(d.get(i))

main_diagonal.append(sum(main_diagonal_initial))


projection_2 = (projection_2_top_final + main_diagonal + projection_2_bottom_final)

print("\nProjection 2")

print(projection_2)



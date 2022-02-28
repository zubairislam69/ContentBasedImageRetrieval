import os
from itertools import islice

import numpy as np
import matplotlib.pyplot as plt

# load and show an image with Pillow
from PIL import Image
import seaborn as sns;

sns.set()

c = '9'
image_name = 'img_10236.jpg'
image_path = os.path.join(os.getcwd(), 'MNIST_DS/' + c, image_name)
print(image_path)
image = Image.open(image_path)

arr = np.asarray(image)

print(arr)

# Projection 1 Start
projection_1 = []

print("\n")

for i in range(28):
    projection_1.append(sum(arr[i]))

print("Projection 1:")
print(projection_1)
# Projection 1 End

d = dict(enumerate(arr.flatten(), 1))

# Projection 2 START

projection_2_top_initial = []
projection_2_top_final = []

projection_2_bottom_initial = []
projection_2_bottom_final = []

main_diagonal_initial = []
main_diagonal = []

split_by_length_top = []
split_by_length_bottom = []

n = 29

for i in range(26):  # 2- 27
    split_by_length_top.append(i + 2)
    split_by_length_bottom.append(27 - i)

for j in range(26):
    for i in range((27 - j), (784 - (725 - (29 * j))), n):  # 29(28-3) want 3 to increment
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

# Projection 2 END


# Projection 3 Start
projection_3_initial = []
projection_3_final = []
split_by_length = []

print("\n")

for j in range(28):
    for i in range(28):
        projection_3_initial.append(arr[i][27 - j])

for i in range(28):
    split_by_length.append(28)

inputt = iter(projection_3_initial)
output = [list(islice(inputt, elem))
          for elem in split_by_length]

for i in range(28):
    projection_3_final.append(sum(output[i]))

print("Projection 3: ")
print(projection_3_final)

# Projection 3 End

# Projection 4 Start

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
    for i in range(756 - (28 * j), 800 - j, n):  # bottom right up to mid diagonal
        projection_4_bottom_initial.append(d.get(i))

    for i in range(27 - j, 730 - (28 * j), n):  # from mid diagonal to top left
        projection_4_top_initial.append(d.get(i))

for j in range(28):
    for i in range(28):
        projection_4_top_initial.append(arr[i][27 - j])  # Top Half Diagonals
        projection_4_bottom_initial.append(arr[i][27 - j])  # Bottom Half Diagonals

input_bottom_P4 = iter(projection_4_bottom_initial)
output_bottom_P4 = [list(islice(input_bottom_P4, elem))
                    for elem in split_by_length_bottom]

input_top_P4 = iter(projection_4_top_initial)
output_top_P4 = [list(islice(input_top_P4, elem))
                 for elem in split_by_length_top]

for i in range(26):
    projection_4_top_final.append(sum(output_top_P4[i]))
    projection_4_bottom_final.append(sum(output_bottom_P4[i]))


for i in range(28, 770, n):  # GETS MAIN DIAGONAL FROM TOP RIGHT TO BOTTOM LEFT
    main_diagonal_initial_P4.append(d.get(i))

main_diagonal_P4.append(sum(main_diagonal_initial_P4))

projection_4 = (projection_4_bottom_final + main_diagonal_P4 + projection_4_top_final)

print("\nProjection 4")
print(projection_4)

# Projection 4 End


def average(p):
    average = round((sum(p) / len(p)), 0)
    return average

# print("proj 4")
#
# sum = 0
# for i in range(54):
#     sum += projection_4[i]


print("Average of P1")
print(average(projection_1))

print("Average of P2")
print(average(projection_2))

print("Average of P3")
print(average(projection_3_final))

print("Average of P4")
print(average(projection_4))


# Convert to 1 and 0
def generate_c(p):
    c = []
    for item in p:
        if item > average(p):
            c.append(1)
        else:
            c.append(0)
    return c


c1 = generate_c(projection_1)
c2 = generate_c(projection_2)

c3 = generate_c(projection_3_final)
c4 = generate_c(projection_4)

print('c1:', c1)
print('c2:', c1)
print('c3:', c3)
print('c4:', c1)

barcode = c1 + c2 + c3 + c4

print(barcode)
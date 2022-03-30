import os
import numpy as np
import matplotlib.pyplot as plt
import time

# load and show an image with Pillow
from PIL import Image
import seaborn as sns

restart = True

while restart:
    start = time.time()

    picNum = 0
    fileNum = 0

    sns.set()

    counter = 0
    d = {}
    dictionary = []

    file = open("barcodes.txt", "w")

    for i in range(10):
        for j in range(10):
            d[counter] = 'img_' + str(i) + str(j) + '.jpg'
            counter = counter + 1

    for i in range(100):
        image_name = d[picNum]
        image_path = os.path.join(os.getcwd(), 'MNIST_DS/' + str(fileNum), image_name)
        # print(image_path)
        image = Image.open(image_path)
        arr = np.asarray(image)

    # Projection 1
        proj_1 = []

        for r in range(28):
            proj_1.append(sum(arr[r]))

        # print("\nProjection 1:")
        # print(proj_1)

    # Projection 2
        proj_2 = []
        for r in range(26, -27, -1):
            proj_2.append(sum(np.diagonal(arr, r)))

        # print("\nProjection 2")
        # print(proj_2)

    # Projection 3
        proj_3 = []
        for r in range(27, -1, -1):
            proj_3.append(sum(arr[:, r]))

        # print("\nProjection 3")
        # print(proj_3)

    # Projection 4
        proj_4 = []
        for r in range(-26, 27):
            proj_4.append(sum(np.fliplr(arr).diagonal(r)))

        # print("\nProjection 4")
        # print(proj_4)

    # Get average of each projection
        def average(p):
            proj_average = round((sum(p) / len(p)), 0)
            return proj_average

        # print("\nAverage of P1")
        # print(average(proj_1))
        #
        # print("Average of P2")
        # print(average(proj_2))
        #
        # print("Average of P3")
        # print(average(proj_3))
        #
        # print("Average of P4")
        # print(average(proj_4))

    # Convert to 1 and 0
        def generate_c(p):
            c = []
            for item in p:
                if item > average(p):
                    c.append(1)
                else:
                    c.append(0)
            return c


        c1 = generate_c(proj_1)
        c2 = generate_c(proj_2)

        c3 = generate_c(proj_3)
        c4 = generate_c(proj_4)

        # print('c1:', c1)
        # print('c2:', c1)
        # print('c3:', c3)
        # print('c4:', c1)

        barcode = c1 + c2 + c3 + c4

        print("\nbarcode for " + image_name)
        print(barcode)


    # length of barcode = 162
        h = ""
        for i in range(162):
            h += str(barcode[i])

        file.write("barcode for " + str(image_name) + ": ")
        file.write(h)
        file.write("\n")
        file.write("\n")



        print()

        # Add all barcode to dictionary with key as image name and value as barcode
        nameAppend = {image_name: barcode}
        dictionary.append(nameAppend)
        # print(dictionary)

        picNum = picNum + 1

        if picNum % 10 == 0:
            fileNum = fileNum + 1

    print(dictionary)
    file.close()

    end = time.time()

    total = end - start
    print("\n")
    print(total)

    answer = input("Would you like to search for another image? ('Y' for yes and 'N' for no)")
    if answer == "N" or answer == "n":
        restart = False
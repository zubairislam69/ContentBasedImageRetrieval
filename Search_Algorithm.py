
# Function for the formula for hamming distance between the bit-strings of barcodes
def hamming_distance(string_1, string_2):
    if len(string_1) == len(string_2):
        d = 0
        for barcode_1, barcode_2 in zip(string_1, string_2):

            if barcode_1 != barcode_2:
                d += 1

        return d
    else:
        return 0


def get_barcodes_data_list(file):
    line = file.readline()
    split_list = []

    while line:
        line = line.strip()
        split_data = line.split(' ')
        split_list.append(split_data)
        line = file.readline()
        line = file.readline()
    return split_list


def find_distance(barcode_list, number):
    size_list_barcode = len(barcode_list)
    str1 = barcode_list[int(number)][3]
    distance_list = []

    for x in range(0, size_list_barcode):
        str2 = barcode_list[x][3]
        res = hamming_distance(str1, str2)
        distance_list.append(res)

    return distance_list


def check_input_number(list_barcode, number):
    check = 0
    for x in range(len(list_barcode)):
        compare_data = list_barcode[x][2][4:6]
        if number == compare_data:
            check = 1
            return check
        else:
            check = -1
    return check


def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]


restart = True

while restart:
    file = open('barcodes.txt', 'r')  # Read The File (barcodes.txt)
    List_barcode = get_barcodes_data_list(file)  # read the read into file and append the List
    number = input('Enter the Image Number that you want to compare from 00-99 : ')  # Get the image number from user
    print("\n")
    check_res = check_input_number(List_barcode, number)  # Check the Input Image number

    if check_res == 1:
        Distance_List = find_distance(List_barcode, number)  # Find the hamming distance
        Distance_List = replace_values(Distance_List, 0, 1000)  # Replace the 0 , 1000
        print('Hamming Distances between the barcodes of the Image Number entered and the rest of the Images : \n',
              Distance_List)  # Display all the Hamming Distances
        print("\n")
        minimum_hamming_distance = min(Distance_List)  # Find the minimum Number
        minimum_index = Distance_List.index(min(Distance_List))  # Find the minimum number Index
        Image_Data = List_barcode[minimum_index][2]  # Get The Image Data of minimum number
        print('The most similar Image is : {} and the Hamming Distance of the Image is: {}'.format(Image_Data,
                                                                                                   minimum_hamming_distance))  # Display the Data

    else:
        print('Please Enter Correct Number : ')

    answer = input("Would you like to search for another image? ('Y' for yes and 'N' for no): ")
    if answer == "N" or answer == "n":
        restart = False

# Function for the formula for hamming distance between the bit-strings of barcodes
def hamming_distance(string_1, string_2):
    if (len(string_1) == len(string_2)):
        d = 0
        for c1, c2 in zip(string_1, string_2):
            # For any difference between the values of 2 barcodes increase the distance by 1
            if c1 != c2:
                d += 1

        return d
    else:
        return 0


# Retrieve barcodes list from the file
def Get_Barcodes_Data_List(File):
    line = File.readline()
    split_list = []

    while line:
        line = line.strip()
        split_data = line.split(' ')
        split_list.append(split_data)
        line = File.readline()
        line = File.readline()
    return split_list


# Function to find the distance comparing all possible combinations of 2 barcodes along the full length of each barcode
def Find_Distance(Barcode_List, number):
    size_list_barcode = len(Barcode_List)
    str1 = Barcode_List[int(number)][3]
    distance_list = []  # Get the distance list in an array

    for x in range(0, size_list_barcode):  # Iterate over every barcode starting
        str2 = Barcode_List[x][3]
        res = hamming_distance(str1, str2)
        distance_list.append(res)

    return distance_list  # Return the distance list

# Checks to see whether the input number is present in the barcode list
def Check_Input_Number(list_barcode, number):
    check = 0
    for x in range(len(list_barcode)):
        compare_data = list_barcode[x][2][4:6]
        if (number == compare_data):
            check = 1
            return check
        else:
            check = -1
    return check


# Function arranges the number of images
def Arrange_Image_Data(image_Data):
    image_syntax = image_Data[:4]
    image_number = int(image_Data[4:6])
    image_name = ''

    if (image_number >= 0 and image_number <= 9):
        image_name = image_syntax + '00' + '.jpg'

    elif (image_number > 9 and image_number <= 19):
        image_name = image_syntax + '01' + '.jpg'

    elif (image_number > 19 and image_number <= 29):
        image_name = image_syntax + '02' + '.jpg'

    elif (image_number > 29 and image_number <= 39):
        image_name = image_syntax + '03' + '.jpg'

    elif (image_number > 39 and image_number <= 49):
        image_name = image_syntax + '04' + '.jpg'

    elif (image_number > 49 and image_number <= 59):
        image_name = image_syntax + '05' + '.jpg'

    elif (image_number > 59 and image_number <= 69):
        image_name = image_syntax + '06' + '.jpg'

    elif (image_number > 69 and image_number <= 79):
        image_name = image_syntax + '07' + '.jpg'

    elif (image_number > 79 and image_number <= 89):
        image_name = image_syntax + '08' + '.jpg'

    elif (image_number > 89 and image_number <= 99):
        image_name = image_syntax + '09' + '.jpg'

    return image_name


# Function Arange the x value
def Arrange_x_value(value):
    number = 0

    if (value >= 0 and value <= 9):
        number = 0

    elif (value > 9 and value <= 19):
        number = 1

    elif (value > 19 and value <= 29):
        number = 2

    elif (value > 29 and value <= 39):
        number = 3

    elif (value > 39 and value <= 49):
        number = 4

    elif (value > 49 and value <= 59):
        number = 5

    elif (value > 59 and value <= 69):
        number = 6

    elif (value > 69 and value <= 79):
        number = 7

    elif (value > 79 and value <= 89):
        number = 8

    elif (value > 89 and value <= 99):
        number = 9

    return number


# function to replace the  numbers
def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]


file = open('barcodes.txt', 'r')  # Read The File (barcodes.txt)
List_barcode = Get_Barcodes_Data_List(file)  # read the read into file and append the List

restart = True

while restart:
    number = input('Enter the Image Number that you want to compare from 00-99 : ')  # Get the image number from user
    print("\n")
    check_res = Check_Input_Number(List_barcode, number)  # Check the Input Image number

    if check_res == 1:
        Distance_List = Find_Distance(List_barcode, number)  # Find the hamming distance
        Distance_List = replace_values(Distance_List, 0, 1000)  # Replace the 0 , 1000
        print('Hamming Distances between the barcodes of the Image Number entered and the rest of the Images : \n',
              Distance_List)  # Display all the Hamming Distances
        print("\n")
        minimum_hamming_distance = min(Distance_List)  # Find the minimum Number
        minimum_index = Distance_List.index(min(Distance_List))  # Find the minimum number Index
        Image_Data = List_barcode[minimum_index][2]  # Get The Image Data of minimum number
        actual_image = Arrange_Image_Data(Image_Data)

        print('The most similar Image is : {} and the Hamming Distance of the Image is: {}'.format(actual_image,
                                                                                                   minimum_hamming_distance))  # Display the Data

    else:
        print('Please Enter Correct Number : ')

    answer = input("Would you like to search for another image? ('Y' for yes and 'N' for no): ")
    if answer == "N" or answer == "n":
        restart = False

# Find the Accuracy


Total_Images = 100
count = 0

for x in range(0, 100):

    Distance_Data = Find_Distance(List_barcode, x)  # find Distance
    Distance_Data = replace_values(Distance_Data, 0, 1000)  # Replace the 0 , 1000
    minimum_hamming_distance = min(Distance_List)  # Find the minimum Number
    Minimum_Data_Index = Distance_Data.index(min(Distance_Data))  # Find the minimum number Index
    image_data = List_barcode[Minimum_Data_Index][2]  # Get The Image Data of minimum number
    Actual_Image = Arrange_Image_Data(image_data)  # Get the Actual Image Number
    Actual_Image = int(Actual_Image[4:6])
    x = Arrange_x_value(x)
    print('the Value of x is : {} and the Value of image is : {}'.format(x, Actual_Image))
    if (x == Actual_Image):  # Check the similar Images and Count
        count += 1

acc = count / Total_Images  # Find the Accuracy

print('Accuracy : {} %'.format(int(acc * 100)))

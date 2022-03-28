
# Function for the formula for hamming distance between the bit-strings of barcodes
def hamming_distance(string_1, string_2):
    if (len(string_1) == len(string_2)):
        d = 0
        for c1, c2 in zip(string_1, string_2):

            if c1 != c2:
                d += 1

        return d
    else:
        return 0


def Get_Barcodes_Data_List(File):
    line = File.readline()
    split_list = []

    while line:
        line = line.strip()
        split_data = line.split(':')
        split_list.append(split_data)
        line = File.readline()
        line = File.readline()

    return split_list

# Calculating hamming distance between each barcode and putting them in an array
def Find_Distance(Barcode_List):
    size_list_barcode = len(Barcode_List)
    str1 = List_barcode[0][1]
    distance_list = []

    for x in range(1, size_list_barcode):
        str2 = Barcode_List[x][1]
        res = hamming_distance(str1, str2)
        str1 = str2
        distance_list.append(res)

    return distance_list


file = open('barcodes.txt', 'r')
List_barcode = Get_Barcodes_Data_List(file)
Distance_List = Find_Distance(List_barcode)
file.close()
print(Distance_List)
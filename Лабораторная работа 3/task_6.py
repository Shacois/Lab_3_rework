list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max = list_numbers[0]
for i in range(len(list_numbers)):
    if list_numbers[i] > max:
        max = list_numbers[i]
        index = i


list_numbers[index], list_numbers[i] = list_numbers[i], list_numbers[index]


print(list_numbers)

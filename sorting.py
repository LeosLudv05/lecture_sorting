import csv
import os

#from cv7.cviceni7 import value


def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(number_array, direction = 'ascending'):
    """

    :param number_array: (list) seznam s numerickou radou
    :param direction: (str) string naznacujici smer razeni
    :return:
    """
    length = len(number_array)
    for i in range(length):
        min_idx = i
        for n in range(i+1, length):
            if direction == "ascending":
                if number_array[n] < number_array[i]:
                    min_idx = n
            elif direction == "descending":
                if number_array[i] > number_array[min_idx]:
                    min_idx = n


        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]
    return number_array

def bubble_sort(number_array):
    """

    :param number_array:  (list) seznam s cislicemi
    :return: serazena num array pomoci bubble sortu
    """
    length = len(number_array)
    for i in range(length - 1):
        for num_idx in range(length - i - 1):
            if number_array[num_idx] > number_array[num_idx + 1]:
                number_array[num_idx], number_array[num_idx + 1] = number_array[num_idx + 1], number_array[num_idx]

    return number_array

def insertion_sort(number_array):
    """

    :param number_array: (list) seznam s cislicemi
    :return: serazena num array pomoci insertion sortu
    """
    length = len(number_array)
    for i in range(1, length):
        key = number_array[i]
        j = i - 1
        while j>= 0 and number_array[j] > key:
            number_array[j + 1] = number_array[j]
            j = j - 1
        number_array[j + 1] = key
    return number_array


def main():
    data = read_data("numbers.csv")
    print(f'Zadaná data: {data}')
    print(selection_sort(data['series_1']))
    print(bubble_sort(data['series_2']))
    print(insertion_sort(data['series_3']))
    pass


if __name__ == '__main__':
    main()

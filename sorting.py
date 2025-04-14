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
                    min_idx = i


        number_array[i], number_array[min_idx] = number_array[min_idx], number_array[i]
    return number_array

def main():
    data = read_data("numbers.csv")
    print(data)
    print(selection_sort(data['series_1']))

    pass


if __name__ == '__main__':
    main()

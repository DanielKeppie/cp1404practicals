"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    list_of_data = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        list_of_data.append(parts)
    input_file.close()
    return list_of_data


def print_data(data):
    for i in range(len(data)):
        data_i = data[i]
        print("{} is taught by {:12} and has {:3} students".format(data_i[0], data_i[1], data_i[2]))


main()

"""
Answer the three questions.
"""

# 1. name.txt
# name = input("Name: ")
# out_file = open("name.txt", "w")
# print(name, file=out_file)
# out_file.close()
#
# # 2. read that.
# in_file = open("name.txt", "r")
# name_of_person = in_file.read()
# print("Your name is {}".format(name_of_person))
# in_file.close()
#
# # 3. numbers.txt
# in_file = open("numbers.txt")
# output = int(in_file.readline()) + int(in_file.readline(2))
# print(output)
# in_file.close()

#4. numbers but more
total = 0
in_file = open("numbers.txt", "r")
for line in in_file:
    current_line = int(line.strip())
    total += current_line
print("{}".format(total))
in_file.close()
"""
Cp1404 practical 05
word_occurrences
"""

word_counter = {}
sentence = input("Text: ")
broken_sentence = sentence.split(" ")
for word in broken_sentence:
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1
list_of_keys = list(word_counter.keys())
list_of_keys.sort()
spacing = [len(key) for key in list_of_keys]
spacing = int(max(spacing)) + 2  # Takes the length of the longest key and adds 2 for : in print statement
print(spacing)
for key in list_of_keys:
    print("{:{}} {}".format((key + " :"), spacing, word_counter[key]))

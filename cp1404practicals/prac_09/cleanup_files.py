"""
CP1404 Practical
Cleanup Files
"""

import os


def main():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):

        for filename in filenames:
            name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            os.rename(name, new_name)


def get_fixed_filename(filename):
    new_file_name = filename[0].upper()  # Sets the first letter to always be upper
    for i in range(1, len(filename)):
        if filename[i].isupper() and filename[i-1].islower():
            new_file_name += "_" + filename[i]
        elif filename[i].isupper():
            new_file_name += filename[i]
        if filename[i].isspace():
            new_file_name += "_"
            continue
        if not filename[i].isidentifier():
            new_file_name += filename[i]
        if filename[i].islower() and not filename[i-1].isalpha() and filename[i-1] != ".":
            # This is a really clunky way of dealing with this one, sorry
            new_file_name += filename[i].upper()
        elif filename[i].islower():
            new_file_name += filename[i]
    new_file_name = new_file_name.replace(".TXT", ".txt")
    return new_file_name


main()

"""
Cp1404 Practical
Daniel Keppie
Sort Files 1
"""

import os
import shutil


def main():
    os.chdir("FilesToSort")
    for filename in os.listdir("."):
        file = filename.split(".")[-1]
        try:
            os.mkdir(file)
        except FileExistsError:
            pass
        os.rename(filename, "{}/{}".format(file, filename))
        shutil.move(filename, file)


main()

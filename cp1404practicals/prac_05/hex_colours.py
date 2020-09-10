"""
CP1404 Practical 05
hex_colours
"""

colours = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "aquamarine": "#7fffd4", "beige": "#f5f5dc",
           "black": "#000000", "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2", "brown": "#a52a2a",
           "burlywood": "#deb887", "cadetblue": "#5f9ea0"}
print(colours)
colour_name = input("Colour name: ")
while colour_name != "":
    try:
        print(colours[colour_name])
    except KeyError:
        print("Invalid colour")
    colour_name = input("Colour name: ")
print("Cheers")

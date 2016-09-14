"""
CP1404/CP5632 Practical
Colour codes in a dictionary
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "DarkGreen": "#006400", "GreenYellow": "#adff2f", "HotPink": "#ff69b4",
                "IndianRed": "#cd5c5c", "MediumSpringGreen": "#00fa9a", "MintCream": "#f5fffa",
                "PaleTurquoise": "#afeeee", "SaddleBrown": "#8b4513", "SteelBlue": "#4682b4"}

for colour in COLOUR_CODES:
    print("{:<20} is {}".format(colour, COLOUR_CODES[colour]))

colour = input("Enter colour name: ")
while colour != "":
    if colour in COLOUR_CODES:
        print(colour, "is", COLOUR_CODES[colour])
        break
    else:
        print("Invalid colour name")
        break
state = input("Enter colour name: ")
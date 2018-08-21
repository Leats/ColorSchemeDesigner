"""
In color theory, "good" color schemes have different harmonies:

complementary
split-complementary
triadic
tetradic
monochrome
"""


def complementary(color):
    """Gives the complementary color given one color saved as string.
    """
    complementaryColor = ""

    try:
        if not isinstance(color, str):
            raise TypeError("color no string!")
        if not validColor(color):
            raise ValueError("string not a valid color")
    except (TypeError, ValueError) as e:
        print(e)
        exit()
    else:
        complementaryColor += complementaryNumber(color[0:2])
        complementaryColor += complementaryNumber(color[2:4])
        complementaryColor += complementaryNumber(color[-2:])
        return(complementaryColor)


def complementaryNumber(number):
    """given a number in hex, returns the "complementary" number for colors"""
    comp = str(hex(abs(int(number, 16) - 255))[2:])
    if len(comp) < 2:
        comp = "0" + comp
    return comp


def validColor(color):
    """checks if given string is a valid color"""
    validChars = "0123456789ABCDEF"

    if len(color) == 6:
        for char in color:
            if char not in validChars:
                return False
        return True
    return False

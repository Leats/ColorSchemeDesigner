"""
In color theory, "good" color schemes have different harmonies:

complementary
split-complementary
triadic
tetradic
monochrome

Color is a list of 3 int values between 0 and 255
"""
from PIL import Image
import random
from conversion import *

def createScheme(color):
    """creates a color scheme with 5 colors and saves them as a file"""
    colors = createComplScheme(color)
    print(colors)

    img = Image.new('RGB', (500, 100), colors[0])
    img.paste(colors[1], [100, 0, 200, 100])
    img.paste(colors[2], [200, 0, 300, 100])
    img.paste(colors[3], [300, 0, 400, 100])
    img.paste(colors[4], [400, 0, 500, 100])
    img.show()

def createComplScheme(color):
    """creates a color scheme with complementary colors"""
    colors = [tuple(color)]
    colors.append(tuple(changeSaturation(color,random.random())))
    colors.append(tuple(complementary(color)))
    colors.append(tuple(changeSaturation(colors[2],random.random())))
    colors.append(tuple(changeBrightness(changeSaturation(colors[2],random.random()),random.random())))
    return(colors)


def randomColor():
    """Creates a random color in list format."""
    return(random.sample(range(255), 3))


def complementary(color):
    """Gives the complementary color given one color saved as string.
    """
    complementaryColor = []

    try:
        if not validColor(color):
            raise ValueError("Given color is not valid!")
    except (TypeError, ValueError) as e:
        print(e)
        print(color)
        exit()
    else:
        for number in color:
            complementaryColor.append(abs(number - 255))
        return(complementaryColor)


def changeSaturation(color, percentage):
    """Changes the saturation of the given color to the given percentage.
    Percentage should be float between 0 and 1."""
    result = RGBtoHSV(color)
    result[1] = percentage
    return(HSVtoRGB(result))

def changeBrightness(color, percentage):
    """Changes the brightness of the given color to the given percentage.
    Percentage should be between 0 and 100."""
    result = RGBtoHSV(color)
    result[2] = percentage
    return(HSVtoRGB(result))


def validColor(color):
    """Checks if given list is a valid color."""
    if len(color) == 3:
        for number in color:
            if number < 0 or number > 255:
                return False
        return True
    return False

createScheme(randomColor())

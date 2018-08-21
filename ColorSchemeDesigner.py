"""
In color theory, "good" color schemes have different harmonies:

complementary
split-complementary
triadic
tetradic
monochrome

Color is a list of 3 int values between 0 and 255
"""


def complementary(color):
    """Gives the complementary color given one color saved as string.
    """
    complementaryColor = []

    try:
        if not isinstance(color, str):
            raise TypeError("Color is no string")
        if not validColor(color):
            raise ValueError("String not a valid color")
    except (TypeError, ValueError) as e:
        print(e)
        exit()
    else:
    	for number in color:
    		complementaryColor.append(abs(number - 255))
        return(complementaryColor)


def complementaryNumber(number):
    """Given a number in hex, returns the "complementary" number for colors."""
    comp = str(hex(abs(int(number, 16) - 255))[2:])
    if len(comp) < 2:
        comp = "0" + comp
    return comp


def saturationChanger(color, percentage):
	"""Changes the saturation of the given color to the given percentage.
	Percentage should be between 0 and 100."""
	pass


def validColor(color):
    """Checks if given list is a valid color."""
    if len(color) == 3:
        for number in color:
            if number < 0 or number > 255:
                return False
        return True
    return False


def toHex(color):
	"""Changes a list containing three int values between 0 and 255 to the
	corresponding hex color as a string."""
	hexColor = ""

	for number in color:
		hexNumber = str(hex(abs(int(number, 16) - 255))[2:])
	    if len(hexNumber) < 2:
	    	# values might only be one digit long, this needs to be changed by a 0 in front
	        hexNumber = "0" + hexNumber
	    hexColor += hexNumber
	return(hexColor)

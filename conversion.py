import math


def RGBtoHEX(color):
    """ Change a list containing three int values between 0 and 255 to the
    corresponding hex color as a string."""
    return(''.join(['%02x' % n for n in color]))


def RGBtoHSV(color):
    """Convert rgb color to hsv color."""
    color = [x / 255 for x in color]

    # checks which element is max
    if color[0] == color[1] == color[2]:
        h = 0
    elif color[0] >= color[1] and color[0] >= color[2]:
        h = 60 * (0 + ((color[1] - color[2]) / (max(color) - min(color))))
    elif color[1] >= color[0] and color[1] >= color[2]:
        h = 60 * (2 + ((color[2] - color[0]) / (max(color) - min(color))))
    elif color[2] >= color[0] and color[2] >= color[1]:
        h = 60 * (4 + ((color[0] - color[1]) / (max(color) - min(color))))
    else:
        print("error getting rgb values")
        exit()
    if h < 0:
        h = h + 360

    if max(color) != 0:
        s = (max(color) - min(color)) / max(color)
    else:
        s = 0

    v = max(color)

    color[0], color[1], color[2] = h, s, v
    return color


def HSVtoRGB(color):
    """Convert hsv color to rgb color."""
    h, s, v = color

    hi = math.floor(h / 60)
    f = (h / 60) - hi
    p = (v * (1 - s))
    q = (v * (1 - s * f))
    t = (v * (1 - s * (1 - f)))

    if hi == 0 or hi == 6:
        color[0], color[1], color[2] = v, t, p
    elif hi == 1:
        color[0], color[1], color[2] = q, v, p
    elif hi == 2:
        color[0], color[1], color[2] = p, v, t
    elif hi == 3:
        color[0], color[1], color[2] = p, q, v
    elif hi == 4:
        color[0], color[1], color[2] = t, p, v
    elif hi == 5:
        color[0], color[1], color[2] = v, p, q
    else:
        print("error changing to rgb")
        exit()
    color = [int(x * 255) for x in color]
    return(color)

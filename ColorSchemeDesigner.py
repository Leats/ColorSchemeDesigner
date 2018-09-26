import random

from PIL import Image

from conversion import HSVtoRGB, RGBtoHSV, RGBtoHEX


def create_scheme(color):
    """Create a color scheme with 5 colors and save them as a file."""

    schemes = [create_compl_scheme, create_mono_scheme, create_split_scheme,
               create_triadic_scheme, create_tetradic_scheme, create_analogous_scheme]

    colors = random.choice(schemes)(color)
    print([RGBtoHEX(c) for c in colors])

    img = Image.new('RGB', (500, 100), colors[0])
    img.paste(colors[1], [100, 0, 200, 100])
    img.paste(colors[2], [200, 0, 300, 100])
    img.paste(colors[3], [300, 0, 400, 100])
    img.paste(colors[4], [400, 0, 500, 100])
    img.show()


def create_compl_scheme(color):
    """Create a color scheme with complementary colors."""
    colors = [tuple(color)]
    colors.append(tuple(change_saturation(color, random.random())))
    colors.append(tuple(complementary(color)))
    colors.append(tuple(change_saturation(colors[2], random.random())))
    colors.append(tuple(change_brightness(change_saturation(
        colors[2], random.random()), random.random())))
    return colors


def create_mono_scheme(color):
    """Create a 'monotone' color scheme. Not completely monotone to
    make it more exciting. Instead, the color will slowly shift in each color. 
    Starting brightness at one point, will shift further down. Since brightness 
    becomes less with each step it should start with at least 58% to not end 
    too dark but start with not more than 98% to not be pure white."""
    brightness = random.uniform(0.588, 0.98)
    colors = [tuple(change_brightness(color, brightness))]
    for x in range(0, 4):
        brightness -= 0.098
        colors.append(tuple(change_brightness(change_hue(colors[0], 9), brightness)))
    return colors


def create_split_scheme(color):
    """Create a color scheme with split complementary colors."""
    colors = [tuple(color)]
    colors.append(tuple(change_brightness(change_saturation(
        color, random.random()), random.random())))
    colors.append(tuple(change_hue(change_saturation(color, random.random()), 150)))
    colors.append(tuple(change_hue(color, -210)))
    colors.append(tuple(change_brightness(change_saturation(
        colors[3], random.random()), random.random())))
    return colors


def create_triadic_scheme(color):
    """Create a color scheme with triadic colors."""
    colors = [tuple(color)]
    colors.append(tuple(change_brightness(change_saturation(
        color, random.random()), random.random())))
    colors.append(tuple(change_hue(change_saturation(color, random.random()), 120)))
    colors.append(tuple(change_hue(color, 240)))
    colors.append(tuple(change_brightness(change_saturation(
        colors[-1], random.random()), random.random())))
    return colors


def create_tetradic_scheme(color):
    """Create a color scheme with tetradic colors."""
    colors = [tuple(color)]
    colors.append(tuple(change_brightness(change_saturation(
        color, random.random()), random.random())))
    colors.append(tuple(change_hue(change_saturation(color, random.random()), 90)))
    colors.append(tuple(change_hue(color, 180)))
    colors.append(tuple(change_brightness(change_saturation(
        change_hue(color, 270), random.random()), random.random())))
    return(colors)


def create_analogous_scheme(color):
    """Create a color scheme with analogous colors."""
    colors = [tuple(color)]
    colors.append(tuple(change_brightness(change_saturation(
        color, random.random()), random.random())))
    colors.append(tuple(change_hue(change_saturation(color, random.random()), 30)))
    colors.append(tuple(change_hue(color, 60)))
    colors.append(tuple(change_brightness(change_saturation(
        change_hue(color, 90), random.random()), random.random())))
    return colors


def random_color():
    """Create a random color in list format."""
    return(random.sample(range(255), 3))


def complementary(color):
    """Give the complementary color given one color saved as string."""
    complementaryColor = []

    try:
        if not valid_color(color):
            raise ValueError("Given color is not valid!")
    except (TypeError, ValueError) as e:
        print(e)
        print(color)
        exit()
    else:
        return [abs(n - 255) for n in color]


def change_saturation(color, percentage):
    """Changes the saturation of the given color to the given percentage.
    Percentage should be float between 0 and 1."""
    result = RGBtoHSV(color)
    result[1] = percentage
    return(HSVtoRGB(result))


def change_brightness(color, percentage):
    """Changes the brightness of the given color to the given percentage.
    Percentage should be between 0 and 100."""
    result = RGBtoHSV(color)
    result[2] = percentage
    return(HSVtoRGB(result))


def change_hue(color, degree):
    """Changes the hue of the given color to the given degree."""
    result = RGBtoHSV(color)
    result[0] += degree
    if result[0] > 360:
        result[0] -= 360
    elif result[0] < 0:
        result[0] += 360
    return(HSVtoRGB(result))


def valid_color(color):
    """Checks if given list is a valid color."""
    if len(color) == 3:
        return all(0 <= n <= 255 for n in color)
    return False

if __name__ == '__main__':
    create_scheme(random_color())

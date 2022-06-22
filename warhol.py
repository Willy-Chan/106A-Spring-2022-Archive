"""
File: warhol.py
---------------
ADD YOUR DESCRIPTION HERE
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

# Name of file that we will use to create the warhol image
IMAGE_FILE = 'images/simba.jpg'




def create_filtered_image(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol program. It creates an
    image object from the image in the file IMAGE_FILE, and then recolors the image
    object.  The parameters to this function are:
      red_scale: A number to multiply each pixels' red component by
      green_scale: A number to multiply each pixels' green component by
      blue_scale: A number to multiply each pixels' blue component by
    This function should return a newly generated image with the appropriately
    scaled color values of the pixels.
    """

    image = SimpleImage(IMAGE_FILE)

    for pixel in image:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale

    return image


def make_warhol():
    """
    This function generates a Warhol-style picture based on the original image in the
    file IMAGE_FILE.  The Warhol image contains "patches" that are different colored
    versions of the original image.  This function returns the Warhol image.
    """
    image = SimpleImage(IMAGE_FILE)
    canvas = SimpleImage.blank(image.width * 3, image.height * 2)

    image_1 = create_filtered_image(1.5, 0, 1.5)
    image_2 = create_filtered_image(1, 1, 1)
    image_3 = create_filtered_image(3, 4, 2)
    image_4 = create_filtered_image(1, 5, 2)
    image_5 = create_filtered_image(9, 1, 8)
    image_6 = create_filtered_image(8, 2, 8)

    for pixel in image_1:
        canvas.set_pixel(pixel.x, pixel.y, image_1.get_pixel(pixel.x, pixel.y))
    for pixel in image_2:
        canvas.set_pixel(image.width + pixel.x, pixel.y, image_2.get_pixel(pixel.x, pixel.y))
    for pixel in image_3:
        canvas.set_pixel(image.width * 2 + pixel.x, pixel.y, image_3.get_pixel(pixel.x, pixel.y))
    for pixel in image_4:
        canvas.set_pixel(pixel.x, pixel.y + image.height, image_4.get_pixel(pixel.x, pixel.y))
    for pixel in image_5:
        canvas.set_pixel(image.width + pixel.x, pixel.y + image.height, image_5.get_pixel(pixel.x, pixel.y))
    for pixel in image_6:
        canvas.set_pixel(2 * image.width + pixel.x, pixel.y + image.height, image_6.get_pixel(pixel.x, pixel.y))

    return canvas

def main():
    """
    This program tests your create_filtered_image and make_warhol functions by calling
    those functions and displaying the resulting images.  Feel free to modify this code
    when you are writing your program.  For example, the call to the create_filtered_image
    function is provided to test that function by itself.  Feel free to delete that portion
    of the code when you have the create_filtered_image working, and then just focus on
    the make_warhol function.
    """
    single_patch = create_filtered_image(1.5, 0, 1.5)
    if single_patch != None:
        single_patch.show()

    warhol_image = make_warhol()
    if warhol_image != None:
        warhol_image.show()


if __name__ == '__main__':
    main()

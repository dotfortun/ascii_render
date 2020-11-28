from PIL import Image


def ascii_image(f_name, font_dim=(16, 16)):
    img: Image.Image = Image.open(f_name)
    return img.resize(
        (img.width//font_dim[0], img.height//font_dim[1]),
        resample=Image.NEAREST
    )

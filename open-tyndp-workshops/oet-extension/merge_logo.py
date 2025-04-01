# -*- coding: utf-8 -*-
from PIL import Image
import sys


def adjust_width(img, base_width=1000):
    wpercent = base_width / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    return img


def adjust_height(img, base_height=1000):
    wpercent = base_height / float(img.size[1])
    wsize = int((float(img.size[0]) * float(wpercent)))
    img = img.resize((wsize, base_height), Image.Resampling.LANCZOS)
    return img


def create_contribution_image(logo_TU, logo_OET):
    x_space = 100

    logo_TU = adjust_height(logo_TU)
    logo_OET = adjust_height(logo_OET)

    widths, heights = zip(*(i.size for i in [logo_TU, logo_OET]))
    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new("RGBA", (total_width + x_space, max_height))

    x_offset = 0
    new_im.paste(logo_TU, (x_offset, 0), mask=logo_TU)
    x_offset += x_space
    x_offset += logo_TU.size[0]
    new_im.paste(logo_OET, (x_offset, 0), mask=logo_OET)

    return new_im


def merge_institue_image(logo_C, logo_I):
    base_width = 4000

    logo_C = adjust_width(logo_C, base_width=base_width)
    logo_I = adjust_width(logo_I, base_width=base_width)

    widths, heights = zip(*(i.size for i in [logo_C, logo_I]))
    max_width = max(widths)
    total_height = sum(heights)

    new_im = Image.new("RGBA", (max_width, total_height))

    y_offset = 0
    new_im.paste(logo_I, (0, y_offset), mask=logo_I)

    y_offset += logo_I.size[1]
    new_im.paste(logo_C, (0, y_offset), mask=logo_C)

    return new_im


logo_TU = Image.open("../logo.png")
logo_OET = Image.open("logo_OET.png")
logo_I = Image.open("../logo_int.png")

logo_C = logo_OET.copy()
logo = merge_institue_image(logo_C, logo_I)

logo.save("../logo_merged.png")

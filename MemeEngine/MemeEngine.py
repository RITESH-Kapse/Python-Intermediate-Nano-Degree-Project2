"""This file is used with MemeEngine module directory, used to draw\
over images."""

import os
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """This class is used to get image,font and related using PIL."""

    def __init__(self, output_dir):
        """Check for output directory & defination of counter variable."""
        self.output_dir = output_dir
        # self.counter = 1

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500) -> str:
        """Create a meme on image and work on it."""
        img = Image.open(img_path)
        outfile = os.path.join(
                               self.output_dir,
                               f"temp-{random.randint(0,10000000)}.jpg"
                               )
        # self.counter += 1
        actual_width, actual_height = img.size
        height = int(actual_height * width / actual_width)
        # img.thumbnail((width, height))

        font1 = ImageFont.truetype("./_data/Fonts/LilitaOne-Regular.ttf", 23)
        font2 = ImageFont.truetype("./_data/Fonts/Roboto-Medium.ttf", 19)

        text_position = random.choice(range(35, height - 50))
        fill_black = (0, 0, 0)
        stroke_fill = (255, 255, 255)

        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), text, fill_black, font1,
                  stroke_width=1, stroke_fill=stroke_fill)
        draw.text((40, text_position + 25), f"- {author}", fill_black, font2,
                  stroke_width=1, stroke_fill=stroke_fill)

        img.save(outfile, "JPEG")
        return outfile

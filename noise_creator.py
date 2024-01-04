import random
from PIL import ImageDraw

def add_noise(img):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for _ in range(random.randrange(4000, 5500)):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

def add_noise_lines(img, number_of_lines=5):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    for _ in range(number_of_lines):
        start_point = (random.randint(0, width), random.randint(0, height))
        end_point = (random.randint(0, width), random.randint(0, height))
        line_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        draw.line([start_point, end_point], fill=line_color, width=2)

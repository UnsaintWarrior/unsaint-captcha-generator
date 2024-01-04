import random, os
import fonts_folder
from PIL import Image, ImageDraw, ImageFont
from filename_utils import filename
from string_generator import random_string
from noise_creator import add_noise, add_noise_lines

def generate_captcha(size):
    def generate_scale_factor(min_scale, max_scale, previous_scale=None):
        scale = random.randint(min_scale, max_scale)
        while scale == previous_scale:
            scale = random.randint(min_scale, max_scale)
        return scale
    scale_factor = generate_scale_factor(min_scale, max_scale)

    def get_random_font(fonts_folder):
        fonts = [f for f in os.listdir(fonts_folder) if f.endswith('.ttf')]
        return os.path.join(fonts_folder, random.choice(fonts)) if fonts else None

    def random_background():
        bg_list = ['white', 'red', 'lime', 'yellow']
        bgColor = random.choice(bg_list)
        return bgColor
    
    bgColor = random_background()

    def generate_image(size, random_string):
        img = Image.new('RGB', size, bgColor)
        draw = ImageDraw.Draw(img)

        font_path = get_random_font('fonts_folder')
        font = ImageFont.truetype(font_path, scale_factor) if font_path else ImageFont.load_default()

        # Load a font
        # font = ImageFont.load_default()

        # Estimate the size of the text (rough estimation)
        # Adjust the scale factor as needed for different fonts or sizes
        # scale_factor = random.randrange(7, 15)
        text_width = len(random_string) * scale_factor
        text_height = scale_factor

        # Calculate the position of the text
        text_x = (size[0] - text_width) / 2
        text_y = (size[1] - text_height) / 2

        # Add text to image
        draw.text((text_x, text_y), random_string, fill="black", font=font)

        # Adiciona ruído à imagem
        add_noise(img)
        add_noise_lines(img)

        img.save(filename)
    generate_image(size, random_string)


if __name__ == '__main__':
    size = 300, 150
    # noise_level = 3500 # Default is 100
    min_scale, max_scale = 25, 28 # Default is 7, 20
    generate_captcha(size)
    print(random_string)
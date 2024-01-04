import os

def generate_filename(base_filename, extension=".png"):
    counter = 0
    unique_filename = f"{base_filename}{counter}{extension}"
    while os.path.exists(unique_filename):
        counter += 1
        unique_filename = f"{base_filename}{counter}{extension}"
    return unique_filename
filename = generate_filename("captcha")
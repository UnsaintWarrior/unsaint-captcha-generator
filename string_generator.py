import random, string

length_list = [5,7,9]

def generate_random_strings(length_list):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    char_length = random.choice(length_list)
    captcha_text = ''.join(random.choice(chars) for _ in range(char_length))
    # print(captcha_text)
    return captcha_text
    
random_string = generate_random_strings(length_list)

if __name__ == '__main__':
    generate_random_strings(length_list = [5,7,9])
    print(random_string)
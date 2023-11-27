import os
import random
import string


def id_generator(size=30, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(_, filename):
    name, ext = get_filename_ext(filename)
    string_random = id_generator()
    final_name = f"{string_random}{ext}"
    return f"tr_images/{final_name}"

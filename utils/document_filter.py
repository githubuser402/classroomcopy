from pathlib import Path

ALLOWED_EXTENSIONS = ('image/jpeg', 'image/png', 'jpeg')

def is_allowed_file(filename):
    return filename in ALLOWED_EXTENSIONS
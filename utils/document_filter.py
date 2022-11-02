from pathlib import Path
import uuid
import os 

ALLOWED_EXTENSIONS = ('image/jpeg', 'image/png', 'jpeg', "text/plain")

def is_allowed_file(filename):
    return filename in ALLOWED_EXTENSIONS


def generate_filename(filename):
    name, extenstion = os.path.splitext(filename)
    return f"{name}_{uuid.uuid4().hex[:10]}{extenstion}"

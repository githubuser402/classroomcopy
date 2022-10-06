from pathlib import Path
from os import path

SECRET_KEY = "JIf9NcHEUBCI3i3tjdD"

TEMPLATES_FOLDER = path.join(Path(__file__).parent.parent, "templates")

STATICFILES_FOLDER = path.join(Path(__file__).parent.parent, "static")
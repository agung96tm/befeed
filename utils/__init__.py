import re
from .http import *


def clean_html(text: str) -> str:
    """ remove html tag from string """
    return re.sub(re.compile('<.*?>'), '', text)

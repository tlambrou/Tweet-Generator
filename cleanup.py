# Module for cleaning up source text

import re

def clean(text):
    return re.sub('[.,:]', '', text)

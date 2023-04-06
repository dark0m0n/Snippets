from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles


LEXERS = []
for item in get_all_lexers():
    if item[1]:
        LEXERS.append(item)

STYLES = []
for i in get_all_styles():
    if i[1]:
        STYLES.append(i)

LEXERS_CHOICES = sorted([(item[1][0], item[0])for item in LEXERS])
STYLES_CHOICES = sorted([(item, item)for item in STYLES])
print(LEXERS_CHOICES)
print(STYLES_CHOICES)
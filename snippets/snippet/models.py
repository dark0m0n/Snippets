from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
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

class Snippet(models.Model):
    titel = models.CharField(max_length=40)
    code = models.TextField()
    languege = models.CharField(max_length=70, choices=LEXERS_CHOICES, default='python')
    style = models.CharField(max_length=70, choices=STYLES_CHOICES, default='igot')
    

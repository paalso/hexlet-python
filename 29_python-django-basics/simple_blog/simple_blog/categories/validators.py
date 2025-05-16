from django.core.exceptions import ValidationError
import re

def validate_latin_characters(value):
    if not re.match(r'^[a-zA-Z0-9\s.,!?\'"-]+$', value):
        raise ValidationError('Название может содержать только латинские буквы, цифры и знаки препинания.')

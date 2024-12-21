import re
from django.core.exceptions import ValidationError


class PasswordValidator:
    def __init__(self, field):
        self.field = field
        print(self.field)

    def __call__(self, value):
        reg_pattern = re.compile(r'^[a-zA-Z0-9]+$')
        tmp_value = dict(value).get(self.field)
        print(tmp_value)
        if not bool(reg_pattern.match(tmp_value)):
            raise ValidationError('Password must contain only letters and numbers')
        return value



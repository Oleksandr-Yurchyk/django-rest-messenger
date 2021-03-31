from django.core.validators import RegexValidator
from django.db import models

# Changed way to regex validations
EMAIL_REGEX = RegexValidator(
    regex=r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$',
    message='This email is not valid.'
)
MESSAGE_REGEX = RegexValidator(
    regex=r'^(?!\s*$)(^[\w\W]{0,100}$)',
    message='Message text can not be blank or longer than 100 characters.'
)


class Message(models.Model):
    author_email = models.CharField(max_length=36, validators=[EMAIL_REGEX])
    text = models.TextField(max_length=100, validators=[MESSAGE_REGEX])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Message id #{self.pk}'

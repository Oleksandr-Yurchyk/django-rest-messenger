import re

email_regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
message_regex = '^(?!\s*$)(^[\w\W]{0,100}$)'


def is_email_valid(email: str):
    return True if re.search(email_regex, email) else False


def is_message_valid(text: str):
    return True if re.search(message_regex, text) else False

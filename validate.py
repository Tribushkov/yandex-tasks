import re

login_pattern = re.compile('^[a-z0-9"!,:._-]+@[a-z0-9_-]+\.[a-z0-9._-]+$')

USER_MAX_LENGTH = 128
DOMAIN_MAX_LENGTH = 256
DOMAIN_MIN_LENGTH = 3
SPECIAL_SYMBOLS = '!,:'


def check_length(user, domain):
    if len(user) > USER_MAX_LENGTH:
        return False
    if len(domain) > DOMAIN_MAX_LENGTH or len(domain) < DOMAIN_MIN_LENGTH:
        return False
    return True


def check_user(user):
    if user.find('..') != -1:
        return False
    return True


def check_domain(domain):
    for chunk in domain.split('.'):
        if len(chunk) == 0:
            return False
        if chunk.startswith('-') or chunk.endswith('-'):
            return False
    return True


def check_quotes(user):
    quote_count = user.count('"')
    if quote_count > 0:
        if quote_count % 2 == 0:
            unquoted = user.split('"')[::2]  # even (unquoted chunks)
            for chunk in unquoted:
                if any(symbol in chunk for symbol in SPECIAL_SYMBOLS):
                    return False
        else:
            return False
    else:
        if any(symbol in user for symbol in SPECIAL_SYMBOLS):
            return False
    return True


def validate_email(email):
    if not login_pattern.match(email):
        return False
    else:
        user, domain = email.split('@')
        return \
            check_length(user, domain) and \
            check_user(user) and \
            check_domain(domain) and \
            check_quotes(user)


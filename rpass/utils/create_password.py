import sys
import secrets
import string
import click


def generate_password(**kwargs):
    """Generate the random password"""
    length = kwargs.get('length')
    upper = kwargs.get('upper')
    lower = kwargs.get('lower')
    no_digits = kwargs.get('no_digits')
    no_symbols = kwargs.get('no_symbols')

    if(length < 1):
        _error("option -l/--length must be greater than zero")

    if(upper and lower):
        _error(
            "option --upper and --lower cannot be used at the same time")

    if(no_digits and no_symbols):
        if(upper):
            seq = string.ascii_uppercase
            return create(length, seq)
        elif (lower):
            seq = string.ascii_lowercase
            return create(length, seq)
        else:
            seq = string.ascii_letters
            return create(length, seq)
    elif (no_symbols):
        if(upper):
            seq = string.ascii_uppercase + string.digits
            return create(length, seq)
        elif (lower):
            seq = string.ascii_lowercase + string.digits
            return create(length, seq)
        else:
            seq = string.ascii_letters + string.digits
            return create(length, seq)
    elif (no_digits):
        if(upper):
            seq = string.ascii_uppercase + string.punctuation
            return create(length, seq)
        elif (lower):
            seq = string.ascii_lowercase + string.punctuation
            return create(length, seq)
        else:
            seq = string.ascii_letters + string.punctuation
            return create(length, seq)
    else:
        seq = string.ascii_letters + string.digits + string.punctuation
        return create(length, seq)


def create(length, seq):
    password = ''.join((secrets.choice(seq) for i in range(length)))
    return "".join(password)


def _error(msg=""):
    click.echo(click.style(f'rpass: error: {msg}', fg="red", bold=True))
    sys.exit(1)

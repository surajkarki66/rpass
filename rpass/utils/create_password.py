import secrets
import string


def generate_password(**kwargs):
    length = kwargs.get('length')
    upper = kwargs.get('upper')
    lower = kwargs.get('lower')
    no_digits = kwargs.get('no_digits')
    no_symbols = kwargs.get('no_symbols')
    if(no_digits and no_symbols):
        if(upper):
            seq = string.ascii_uppercase
            return create(length, seq)
        if(lower):
            seq = string.ascii_lowercase
            return create(length, seq)
        seq = string.ascii_letters
        return create(length, seq)
    if(no_symbols):
        if(upper):
            seq = string.ascii_uppercase + string.digits
            return create(length, seq)
        if(lower):
            seq = string.ascii_lowercase + string.digits
            return create(length, seq)
        seq = string.ascii_letters + string.digits
        return create(length, seq)
    if(no_digits):
        if(upper):
            seq = string.ascii_uppercase + string.punctuation
            return create(length, seq)
        if(lower):
            seq = string.ascii_lowercase + string.punctuation
            return create(length, seq)
        seq = string.ascii_letters + string.punctuation
        return create(length, seq)

    seq = string.ascii_letters + string.digits + string.punctuation
    return create(length, seq)


def create(length, seq):
    password = ''.join((secrets.choice(seq) for i in range(length)))
    return "".join(password)

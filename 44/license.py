import secrets
import string

alphabet = string.ascii_uppercase + string.digits


def gen_key(parts=4, chars_per_part=8):
    """ generates n parts of random sequence of upper case letters and numbers
    each with length of chars_per_part and separated with '-' """
    return "-".join(
        [_gen_random_alphanumeric_seq(chars_per_part) for i in range(parts)]
    )


def _gen_random_alphanumeric_seq(num_characters):
    """ helper function for gen_key which returns a random string of letters and
    numbers with length num_characters """
    return "".join(secrets.choice(alphabet) for i in range(num_characters))

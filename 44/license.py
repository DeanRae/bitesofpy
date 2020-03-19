import secrets
import string

alphabet = string.ascii_uppercase + string.digits


def gen_key(parts=4, chars_per_part=8):
    pass


def _gen_random_alphanumeric_seq(num_characters):
    """ helper function for gen_key which returns a random string of letters and
    numbers with length num_characters """
    return "".join(secrets.choice(alphabet) for i in range(num_characters))

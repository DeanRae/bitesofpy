def get_index_different_char(chars):
    """ store two separate lists of non-alpha and alphanumeric characters. Its values are the indexes of the given chars array. Returns the first element of the shorter list as this is the one containing the odd element """

    non_alnum_chars = []
    alnum_chars = []

    for index, char in enumerate(chars):
        if str(char).isalnum():
            alnum_chars.append(index)
        else:
            non_alnum_chars.append(index)

    return (
        alnum_chars[0]
        if len(alnum_chars) < len(non_alnum_chars)
        else non_alnum_chars[0]
    )


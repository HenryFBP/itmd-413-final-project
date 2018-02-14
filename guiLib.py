hex_digits = "0123456789ABCDEF"


def random_hex_digit():
    """
    Return a random single-digit hex string.
    :return: The hex string.
    Example:
    r_h_d() -> "E"
    """
    return hex_digits[random.randrange(0, len(hex_digits))]


def random_hex_string(l=6):
    """
    Return a random hex color string.
    :param l: How long the hex string will be.
    :return: The hex string.
    Example:
    r_h_s(l=3) -> "A0E"
    r_h_s(l=1) -> "F"
    """
    s = ""
    for i in range(l):
        s += random_hex_digit()
    return s

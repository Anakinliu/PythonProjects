def get_formatted_name(first, last, middle):
    """
    generate a neatly formatted full name
    :param first:
    :param middle:
    :param last:
    :return: formatted full name
    """

    full_name = first + ' ' + middle + ' ' + last
    return full_name.title()
#!/usr/bin/python3
"""Text Indentation"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (str): Text to transform and print.

    Raises:
        TypeError: If `text` is not a string.
    """
    if type(text) != str:
        raise TypeError("text must be a string")

    buf = ""
    for ch in text:
        buf += ch
        if ch in ".?:":
            print(buf.strip(), end="\n\n")
            buf = ""
    if buf != "":
        print(buf.strip(), end="")

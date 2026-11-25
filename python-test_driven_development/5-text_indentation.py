#!/usr/bin/python3
"""Print text with paragraph breaks after selected punctuation."""


def text_indentation(text):
    """Print text with spacing after periods, question marks, and colons."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    start = 0
    for index, character in enumerate(text):
        if character in ".?:":
            line = text[start:index + 1].strip(" ")
            print("\n".join(part.strip(" ") for part in line.split("\n")),
                  end="\n\n")
            start = index + 1
    rest = text[start:].split("\n")
    print("\n".join(part.strip(" ") for part in rest), end="")

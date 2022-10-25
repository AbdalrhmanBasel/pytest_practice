"""
    TODO:
        1. Build Regex pattern for youtube video links.
        2. Get input from user and validate links.

        Make a console program that takes a YouTube video link and validates it with a regular expression
        Checking all options should be done with only one regular expression

        Link options:
        https://www.youtube.com/watch?v=zI48YAa-Jec
        https://youtu.be/zI48YAa-Jec
        https://youtu.be/zI48YAa-Jec?t=1
        https://www.youtube.com/watch?v=zI48YAa-Jec&t=1
"""

import re

link = input("Enter Youtube Link: ")


def YT_link_Validitor(link):
    REGEX = '(?:https?:\/\/)?(?:www\.)?youtu\.?be(?:\.com)?\/?.*(?:watch|embed)?(?:.*v=|v\/|\/)([\w\-_]+)\&?.*'
    if re.search(REGEX, link):
        return print("Valid Youtube Link.")
    else:
        return print("Not valid Youtube Link.")


YT_link_Validitor(link)

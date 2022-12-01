"""
    TODO:
        Link Normalization Test
        - In this task and the next one, you need to collect a list of links of pictures and download them.
        - You will find problems when specifying the protocol, domain, etc, in the links.
        - Write a function to normalize the link of the picture. (Code can be partially taken from previous tasks)
        - Function must accept link of the image and the domain of the current page to substitute the domain in the link.
        - The function writen must return the corrected reference.
        - then you will have to write tests using Pytest.
        - Write options for input values for the test.
        - https://http.cat/200.jpg - norms
        - http.cat/200.jpg - without protocol (you need to add http)
        - 200.jpg - without a domain (it will work, this picture is on a page inside this site)

    TODO:
        1. Write a function that check if http: exist and if not, add the http: protocol.
        2. Write tests that fix the links if it was wrong by adding http: if it didn't exist.
"""

list = ['https://http.cat/200.jpg ', '//http.cat/200.jpg']

class Link_normalization:

    REGEX = '(https?:\/\/(?:www\.).*.*'

    def link_fixer(self, list):
        if re.search(REGEX, link):
            return print("Valid Youtube Link.")
        else:
            return print("Not valid Youtube Link.")

# /https?:\/\/(?:www\.).*.*/gm
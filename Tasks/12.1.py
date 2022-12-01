'''
TODO:
    - Normalize Text.
    - Pytest if it is valid response.
'''

import re
import requests


url = 'google.com/'


class Link_Validator:


    @staticmethod
    def link_statue(url):
        r = requests.head(url)
        return r.status_code == 200
    @staticmethod
    def link_regex(url):
        regex = 'https?:\/\/(?:www\.).*.*'
        if re.search(regex, url):
            return print("Valid Link.")
        else:

            return print("Not valid Link.")

    @staticmethod
    def normalize_url(url):
        """Prefix a schema-less URL with http://."""
        protocol = "https://"
        if 'www' not in url:
            url = protocol + 'www.' + url
        return url


# class Test_Link_Validator:
#     def test_one(self):
#         # regex = 'https?:\/\/(?:www\.).*.*'
#         # assert re.search(regex, url)
#         assert url.status_code == 200



if __name__ == "__main__":
    link = Link_Validator()
    fixed = link.normalize_url(url)
    print(link.normalize_url(url))
    link.link_statue(fixed)

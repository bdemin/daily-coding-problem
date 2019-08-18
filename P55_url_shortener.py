# Implement a URL shortener with the following methods:

# shorten(url), which shortens the url into a six-character alphanumeric string, such as zLg6wl.

# restore(short), which expands the shortened string into the original url.
# If no such shortened string exists, return null.
# Hint: What if we enter the same URL twice?


import hashlib


class UrlShortener(object):
    def __init__(self):
        self.url_database = dict()
        self.hash_func = hashlib.sha256
        self.domain = "http://short.url/"


    def shorten(self, url):
        output_hash = self.hash_func(url.encode()).hexdigest()
        short_hash = output_hash[:6]
        self.url_database[short_hash] = url
        return self.domain + short_hash


    def restore(self, short):
        short_hash = short.replace(self.domain, "")
        return self.url_database[short_hash]

# Driver code
url = 'http://www.google.com/'
url_shortener = UrlShortener()
print('Shortened: ', url_shortener.shorten(url))
print('Original: ', url_shortener.restore(url_shortener.shorten(url)))

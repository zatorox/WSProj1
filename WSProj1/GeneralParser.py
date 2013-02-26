import urllib
import json

from Browser import Browser, BrowserError

class SearchError(Exception):
    """
    Base class for search exceptions.
    """
    pass

class FarooSearch(object):

    SEARCH_URL = "http://www.faroo.com/api?q=%(query)s&start=%(start)s&length=%(length)s&l=en&src=web&f=json"

    def __init__(self, query, start, length):
        self.query = query.replace(' ', '%20')
        self.start = start
        self.length = length
        self.browser = Browser()

    def _get_results(self):

        url = FarooSearch.SEARCH_URL
        
        actual_url = url % {'query': self.query,
                         'start': self.start,
                         'length': self.length}

        try:
            page = self.browser.get_page(actual_url)
        except BrowserError:
            raise SearchError ("Failed getting %s: %s") % (e.url, e.error)

        print("'''" + page.decode("utf-8") + "'''")
        return "'''" + page.decode("utf-8") + "'''"
        


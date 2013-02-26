import urllib
import json

from Browser import Browser, BrowserError
from PageResult import PageResult

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

        return page.decode("utf-8")

class StringParser(object):

    def __init__(self, results):
        self.results = results

    def _convertToList(self):
        results2 = self.results.replace('''"news": false,''',"")
        results3 = results2.replace('''"news": true,''',"")
        
        data = json.loads(results3)

        pageResults = [PageResult(data['results'][i]['title'],
                                 data['results'][i]['kwic'],
                                 data['results'][i]['content'],
                                 data['results'][i]['url'],
                                 data['results'][i]['iurl'],
                                 data['results'][i]['domain'],
                                 data['results'][i]['author'],
                                 data['results'][i]['votes'],
                                 data['results'][i]['date']) for i in range(len(data['results']))]

        return pageResults
        


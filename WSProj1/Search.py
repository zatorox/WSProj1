import PageSort
from PageResult import PageResult
from Browser import Browser, BrowserError

def Search(keyword):
    print "searching for: " + keyword
    relatedWords = ["Wheel", "Model"]
    searchResults = [
                     PageResult("Volvo", "This car has a lot of wheels is also a great car model", None, None, None, None, None, None, None),
                     PageResult("Mercedes", "This car has a lot of wheels and is a great model", None, None, None, None, None, None, None)
                    ]


    return PageSort.Sort(searchResults, relatedWords)
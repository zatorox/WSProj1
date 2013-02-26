import PageSort

from PageResult import PageResult
from GeneralParser import FarooSearch, SearchError, StringParser

def Search(keyword):
    try:
        fs = FarooSearch(keyword, "1", "8")
        results = fs._get_results()
        sp = StringParser(results)
        resultList = sp._convertToList()
    except SearchError as e:
        print ("Search failed: %s", e)
    
    print('searching for: ' + keyword)
    relatedWords = ["Wheel", "Model"]

    return PageSort.Sort(resultList, relatedWords)
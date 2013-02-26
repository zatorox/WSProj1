from GeneralParser import FarooSearch, SearchError, StringParser

try:
    fs = FarooSearch("iPhone", "1", "10")
    results = fs._get_results()
    sp = StringParser(results)
    resultList = sp._convertToList()
except SearchError as e:
    print ("Search failed: %s", e)
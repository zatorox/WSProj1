from GeneralParser import FarooSearch, SearchError

try:
    fs = FarooSearch("quidditch", "1", "5")
    results = fs._get_results()
except SearchError:
    print ("Search failed: %s")


from GeneralParser import FarooSearch, SearchError

try:
    fs = FarooSearch("quidditch", "1", "5")
    #gs.results_per_page = 50
    results = fs._get_results()
except SearchError:
    print ("Search failed: %s") % e



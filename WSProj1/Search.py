from PageSort import PageSort
from PageResult import PageResult

relatedWords = ["Wheel", "Model"]
searchResults = [
                 PageResult("Volvo", "This car has a lot of wheels", None, None, None, None, None, None, None, None),
                 PageResult("Mercedes", "This car has a lot of wheels and is a great model", None, None, None, None, None, None, None, None)
                ]
print self.PageSort.Sort(searchResults, relatedWords)
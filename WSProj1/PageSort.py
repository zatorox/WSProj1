import PageResult

def Sort(pageResults, relatedWords):
    pageHitMapping = {}
    for pageResult in pageResults:
        pageHitMapping[pageResult] = 0;
        for relatedWord in relatedWords:
            pageHitMapping[pageResult] += pageHitMapping[pageResult].kwic.count(relatedWord)
        
    sortedPages = []
    for key, value in sorted(pageHitMapping.iteritems(), key=lambda(k,v): (v,k)):
        sortedPages.append(key)

    return sortedPages



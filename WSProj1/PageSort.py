def Sort(pageResults, relatedWords):
    pageHitMapping = {}
    for pageResult in pageResults:
        pageHitMapping[pageResult] = 0;
        for relatedWord in relatedWords:
            pageHitMapping[pageResult] += pageResult.kwic.count(relatedWord)
        
    sortedPages = []
    '''for key, value in sorted(pageHitMapping.iteritems(), key=value):
        sortedPages.append(key)'''
    return pageResults



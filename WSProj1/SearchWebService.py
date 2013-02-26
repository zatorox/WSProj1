from bottle import route, run, template

import Search

@route('/:keyword', method='GET')
def get_event(keyword):
    jsonOutput = "{\"results\":["
    for searchResult in Search.Search(str(keyword)):
        jsonOutput += searchResult.jsonSeralize() + ","

    if jsonOutput.endswith(','):
        jsonOutput = jsonOutput[:-1]
   

    jsonOutput += "]}"
    return jsonOutput

run(host='localhost', port=8080)
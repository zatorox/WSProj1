import json

class PageResult:

    def __init__(self, title, kwic, content, url, iurl, domain, author, votes, date):
        self.title = title
        self.kwic = kwic
        self.content = content
        self.url = url
        self.iurl = iurl
        self.domain = domain
        self.author = author
        self.votes = votes
        self.date = date

    def jsonSeralize(self):
        '''return "{" + self.serializeKeyValue("title", self.title) + "," + self.serializeKeyValue("kwic", self.kwic) + "," + self.serializeKeyValue("content", self.content) + "," + self.serializeKeyValue("url", self.url) + "," + self.serializeKeyValue("iurl", self.iurl) + "," + self.serializeKeyValue("domain", self.domain) + "," + self.serializeKeyValue("author", self.author) + "," + self.serializeKeyValue("votes", self.votes) + "," + self.serializeKeyValue("date", self.date) + "}"'''
        return "{" + self.serializeKeyValue("title", self.title) + "}"

    def serializeKeyValue(self, key, value):
        if value == None:
            return "\"" + key + "\": \"\""
        return "\"" + key + "\": \"" + value + "\""
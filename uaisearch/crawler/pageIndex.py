__author__ = 'bruno'


class PageIndex(object):
    def __init__(self):
        self.index = {}

    def add_to_index(self, url, keyword):
        for entry in self.index:
            if entry[0] == keyword:
                entry[1].append(url)
                return

    def lookup(self, keyword):
        for entry in self.index:
            if entry[0] == keyword:
                return entry[1]

        return []

    def add_page_to_index(self, url, content):
        words = content.split()
        for word in words:
            self.add_to_index(word, url)
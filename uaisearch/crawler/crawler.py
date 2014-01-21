__author__ = 'bruno'
import urllib.request
from uaisearch.crawler.pageIndex import PageIndex
import uaisearch.crawler.util.pageUtils as PageUtils


class Crawler(object):
    def __init__(self, seed):
        self.to_crawl = [seed]
        self.crawled = []
        self.index = PageIndex()
        self.graph = {}

    def start(self):
        while self.to_crawl:
            url = self.to_crawl.pop()
            if url not in self.crawled:
                page = urllib.request.urlopen(url)
                content_page = page.read().decode('utf8')
                self.index.add_page_to_index(page, content_page)
                out_links = PageUtils.get_all_links(content_page)
                self.graph[url] = out_links
                self.crawled.append(url)

                for link in out_links:
                    if link not in self.crawled:
                        self.to_crawl.append(link)
        return self.index, self.graph



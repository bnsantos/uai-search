__author__ = 'bruno'


def get_next_target(page):
    start_line = page.find('<a href=')
    if start_line == -1:
        return None, 0
    start_quote = page.find('"', start_line)
    end_quote = page.find('"', start_quote+1)
    if start_quote == -1 or end_quote == -1:
        return None, 0
    url=page[start_quote+1: end_quote]
    return url, end_quote


def get_all_links(page):
    urls = []
    while True:
        url, end_pos = get_next_target(page)
        if url:
            urls.append(url)
            page = page[end_pos:]
        else:
            break

    return urls

from lxml import html


class HTMLParser:
    def get_elements_by_xpath(self, source, xpath):
        tree = html.fromstring(source)
        return tree.xpath(xpath)


html_parser = HTMLParser()

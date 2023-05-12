from lxml import etree

html = etree.parse('test.html', etree.HTMLParser())
result = html.xpath('//li[contains(@class,"li-first")]/a/text()')
print(result)

from parsel import Selector

html = '''
<div>
    <ul>
        <li class="item-0"><a href="link1.html">first item</a></li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1" active><a href="link4.html">forth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
</div>
'''

selector = Selector(text=html)
items = selector.xpath('//li[contains(@class,"item-0")]')
# 提取文字
# for item in items:
#     text = item.xpath('.//text()').get()
#     print(text)
# result = selector.xpath('//li[contains(@class,"item-0")]//text()').getall()
# print(result)
# 提取属性
result = selector.xpath('//li[contains(@class,"item-0") and contains(@class,"active")]/a/@href').get()
print(result)

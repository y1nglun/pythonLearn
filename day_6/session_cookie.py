"""
Session和Cookie:
    Session:在服务端,用来保存用户的Session信息.Session对象用来存储特定用户Session所需的
        属性及配置信息,当用户在程序的页面之间进行跳转时,存储在Session对象中的变量将不会丢失
        会在整个用户Session中一直存在下去
    Cookie:在客户端,浏览器在下次访问相同网页时,就会自动附带上Cookie,并发送给服务器,
        服务器通过识别Cookie鉴定出是哪个用户在访问,然后判断此用户是否处于登录状态,
        并返回对应的响应

    Session维持:
        在客户端第一次请求服务器时,服务器会返回一个响应头中带有Set-Cookie字段的响应给客户端.
        客户端把Cookie保存起来,当下一次请求相同的网站时,把保存起来的Cookie放在请求头中一起
        提交给服务器.Cookie中携带着Session ID相关信息,服务器通过检测Cookie即可找到对应的
        Session,继而通过判断Session辨认用户状态.
        Session和Cookie需要配合,一个在客户端,一个在服务端,二者相互协同,就实现了登陆控制
"""
import urllib.request
import urllib.parse

url = 'https://www.httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'Host': 'www.httpbin.org'
}
dic = {'name': 'germey'}
data = bytes(urllib.parse.urlencode(dic), encoding='utf-8')
req = urllib.request.Request(url=url, data=data, headers=headers, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))

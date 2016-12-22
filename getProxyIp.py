#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup

class ProxyX:
    def __init__(self, url):
        self.url = url
        self.pool={}
    def get_pool(self):
        self.fill_pool()
        return self.pool
    def fill_pool(self):
        pass

class Proxy360(ProxyX):
    def __init__(self):
        self.url = "http://www.proxy360.cn/default.aspx"
        ProxyX.__init__(self, self.url)

    def fill_pool(self):
        r = requests.get(self.url)
        bso = BeautifulSoup(r.text, 'html.parser')
        proxyList = bso.findAll('div',{'class':'proxylistitem'})
        iplist = [proxy.get_text().split('\n') for proxy in proxyList]
        #ip_str_list = [','.join([j.strip() for j in i]) for i in iplist]
        ip_str_list = [','.join([j.strip() for j in i]) for i in iplist]
        poollist=[ipstr.replace(',,,',' ').strip().split(' ') for ipstr in ip_str_list]
        pool = {':'.join(i[:2]):i for i in poollist}
        self.pool = pool

class ProxyXici(ProxyX):
    def __init__(self):
        self.url = "http://www.xicidaili.com/nn/"
        ProxyX.__init__(self, self.url)

    def fill_pool(self):
        headers = {
        'Host': 'www.xicidaili.com',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'DNT': '1',
        'Referer': 'http://www.xicidaili.com/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8'
        #'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWRiYjMzMjA0NzRlOGY0ZTJlNmYyMGI4MTcxY2ViYTY4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUxOYnNMN1AzNUd1NGVrTEZteWNkcU1haVF2UldKZklLc05KMnQ1dVFwWVE9BjsARg%3D%3D--8b9543c4010c93f6ea66796717efb4aadb519d38; CNZZDATA1256960793=1937703299-1482385062-null%7C1482385062'
        }
        r = requests.get(self.url, headers=headers)
        bso = BeautifulSoup(r.text, 'html.parser')

import requests
import re
import logging
import ujson

logger = logging.getLogger('''sourceDns.webdns.views''')
header = {
    '''User-Agent''': '''Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 '''
                  '''(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'''
}


class Base:
    def __init__(self, url):
        self.url = url


class Data(Base):
    def __init__(self, url, **kwargs):
        super(Data, self).__init__(url)

    def request(self):
        try:
            req = requests.get(self.url, timeout=5, headers=header)
            content = req.text
            req.close()
            return content
        except Exception as e:
            logger.error(e)
            return False


class ZhiLian(Data):
    def handle(self):
        content = self.request()
        try:
            msg = ujson.loads(content)
        except Exception as e:
            logger.error(e)
            msg = {}
        if msg and msg.get('code'):
            return msg['data']['results']

    def get_data(self, content):
        for con in content:
            pass

    def get_details(self, url):
        try:
            req = requests.get(url, headers=header)
            if req.status_code is 200:
                return req.text
        except Exception as e:
            logger.error(e)
            return
# url = '''https://fe-api.zhaopin.com/c/i/sou?start=60&pageSize=60&cityId=530&industry=10100&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&lastUrlQuery=%7B%22jl%22:%22530%22,%22in%22:%2210100%22,%22kw%22:%22Python%22,%22kt%22:%223%22%7D'''
# a = ZhiLian(url)
# print(a.handle())


class LiePin(Data):
    def handle(self):
        content = self.request()
        start = content.find('''<ul class="sojob-list">''')
        end = content.rfind('''<div class="pager">''')
        info = content[start: end]
        parttern = re.compile(r'''<[^>]+>''', re.S)
        data = parttern.sub('''''', info)

        msg = data.replace(''' ''', '''''')
        message = re.compile(r'''/\t+''', re.S).sub('''''', msg)
        ret = message.split('''\r\n''')
        result = [r.replace('''\t''', '''''') for r in ret if '''\t''' in r and r]
        while '''''' in result:
            result.remove('''''')
        return result

b = '''https://fe-api.zhaopin.com/c/i/sou/page-title?start=60&pageSize=60&cityId=530&areaId=&businessarea=%7B%7D&industry=10100&salary=&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&jobType=-1&sortType=&kw=Python&kt=3&bj=&sj=&lastUrlQuery=%7B%22p%22:2,%22jl%22:%22530%22,%22in%22:%2210100%22,%22kw%22:%22Python%22,%22kt%22:%223%22%7D'''

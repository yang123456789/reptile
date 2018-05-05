import requests
import re
import logging

logger = logging.getLogger('sourceDns.webdns.views')


class Base:
    def __init__(self, url):
        self.url = url


class Data(Base):
    def __init__(self, url, **kwargs):
        super(Data, self).__init__(url)

    def request(self):
        try:
            req = requests.get(self.url, timeout=5)
            content = req.text
            req.close()
            return content
        except Exception as e:
            logger.error(e)
            return False


class ZhiLian(Data):
    def handle(self):
        content = self.request()
        start = content.find('<table width="853" class="newlist" cellpadding="0" cellspacing="0">')
        end = content.rfind('</table>')
        info = content[start: end+8]
        parttern = re.compile(r'<[^>]+>', re.S)
        data = parttern.sub('', info)
        msg = data.replace(' ', '')
        ret = msg.split('\r\n')
        result = list()
        for r in ret[1:]:
            if r != '':
                result.append(r)
        return result


class LiePin(Data):
    def handle(self):
        content = self.request()
        start = content.find('<ul class="sojob-list">')
        end = content.rfind('<div class="pager">')
        info = content[start: end]
        parttern = re.compile(r'<[^>]+>', re.S)
        data = parttern.sub('', info)

        msg = data.replace(' ', '')
        message = re.compile(r'/\t+', re.S).sub('', msg)
        ret = message.split('\r\n')
        result = [r.replace('\t', '') for r in ret if '\t' in r and r]
        while '' in result:
            result.remove('')
        return result

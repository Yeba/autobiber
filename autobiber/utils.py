import requests
from fake_useragent import UserAgent
from requests.adapters import HTTPAdapter
import urllib3
from urllib3.util.ssl_ import create_urllib3_context
import random
from multiprocessing.dummy import Pool as ThreadPool

# 反爬
ORIGIN_CIPHERS = ('ECDH+AESGCM:DH+AESGCM:ECDH+AES256:DH+AES256:ECDH+AES128:DH+AES:ECDH+HIGH:'
                  'DH+HIGH:ECDH+3DES:DH+3DES:RSA+AESGCM:RSA+AES:RSA+HIGH:RSA+3DES')
# 消除warning
urllib3.disable_warnings()


class DESAdapter(HTTPAdapter):
    def __init__(self, *args, **kwargs):
        """
        A TransportAdapter that re-enables 3DES support in Requests.
        """
        CIPHERS = ORIGIN_CIPHERS.split(':')
        random.shuffle(CIPHERS)
        CIPHERS = ':'.join(CIPHERS)
        self.CIPHERS = CIPHERS + ':!aNULL:!eNULL:!MD5'
        super().__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).init_poolmanager(*args, **kwargs)

    def proxy_manager_for(self, *args, **kwargs):
        context = create_urllib3_context(ciphers=self.CIPHERS)
        kwargs['ssl_context'] = context
        return super(DESAdapter, self).proxy_manager_for(*args, **kwargs)


class reqSpider:
    def __init__(self):
        self.ua = UserAgent()

    def get_raw_txt(self, url):
        if not url.startswith('http'):
            url = 'http://' + url
        try:
            s = requests.Session()
            s.headers.update({
                # ua.random 表示的时 随机生成一个User-Agent，这样的话我们就能有很多个 User-Agent 来使用，就不用再担心 被封ip了。
                "User-Agent": self.ua.random,
                'Referer': url,
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Accept-Language": "zh-CN,zh;q=0.9",
                "Accept-Encoding": "gzip, deflate, br",
                "DNT": "1",
                "Connection": "close"
            })
            s.mount('http://', DESAdapter())
            s.mount('https://', DESAdapter())
            resp = s.get(url, verify=False)
            return resp.text
        except:
            return None

def _f(arg):
    return arg[0](*arg[1:])

def execPool(func, args, pool_size=8, ):
    pool = ThreadPool(pool_size)
    for i in range(len(args)):
        args[i].insert(0,func)
    res = pool.map(_f, args)
    pool.close()
    pool.join()
    return res

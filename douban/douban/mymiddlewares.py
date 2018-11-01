import random
# from umei.settings import USER_AGENTS
import base64

class RandomUserAgent(object):
    def __init__(self):
        self.user_agent = [
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
            'Mozilla/5.0 (Windows NT 6.1; rv,2.0.1) Gecko/20100101 Firefox/4.0.1',
        ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agent)


class RandomProxy(object):
    def __init__(self):
        self.proxy = {'ip_port': '121.42.140.113:16816', 'user_pwd': 'mr_mao_hacker:sffqry9r'}

    def process_request(self, request, spider):
        proxy = random.choice(self.proxy)
        #对没有代理用户认证的处理
        if self.proxy['user_pwd'] == '':
            request.meta['proxy'] = 'https://' + self.proxy['ip_port']
        else:

            #对账户密码进行base64转码
            base64_user_pwd = base64.b64encode(self.proxy['user_pwd'])
            #对应代理服务器的信令格式进行输出
            request.headers['Proxy-Authorzation'] = 'Basic '+base64_user_pwd
            request.meta['proxy'] = 'https://' + self.proxy['ip_port']
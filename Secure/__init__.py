import os
class Domain:
    def __init__(self, domain, port, protocol):
        self.domain = domain
        self.port = port
        self.protocol = protocol

    #  构造一个URL
    def url(self):
        if self.protocol == 'https':
            url = 'https://' + self.domain + ':' \
            + 'self.port' + '/'
        if self.protocol == 'http':
            url = 'http://' + self.domain + ':' \
                  + self.port + '/'
            return url

    # 调用os.system中的主机命令lookup去解析域名
    def lookup(self):
        os.system("host " + self.domain)

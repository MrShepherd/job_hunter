import hashlib


class Md5(object):
    def __init__(self, s):
        self.s = s

    def md5(self):
        # print(hashlib.md5(self.s.encode('utf-8')).hexdigest())
        return hashlib.md5(self.s.encode('utf-8')).hexdigest()

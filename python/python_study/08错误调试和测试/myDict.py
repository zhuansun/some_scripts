import logging

# 我的字典类
class Dict(dict):

    # 初始化方法，调用Dict的默认的初始化方法
    def __init__(self,**kw):
        super().__init__(**kw)


    # get方法
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError as e:
            logging.exception(e)

    # set方法
    def __setattr__(self, key, value):
        self[key] = value



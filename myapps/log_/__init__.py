import logging

logging.getLogger().setLevel(logging.WARNING)

#配置日志的格式与处理器(FileHandler)
#可以自定义日志的格式  %(格式名)s，在日志输入消息时，使用extra={'格式名':'消息值'}
logging.basicConfig(format='%(asctime)s: %(filename)s/%(funcName)s '
                           'at %(lineno)s of user %(username)s->%(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='art.log',
                    filemode='a')
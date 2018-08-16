from HartPro.celery import app
import time
from redis_ import rd

@app.task
def qdTask(uid,aid):
    '''
    异步执行抢读功能
    :param uid: 用户id
    :param aid: 文章id
    :return:
    '''

    #判断qdArt的hash项是否已达到最大值(5本书)
    if rd.hlen('qdArt') == 5:
        return '抢读失败'

    #将用户id和aid存入到hash中
    #adArt 可以被设计成'活动ID:qdArt'

    #优化代码，避免同一个人抢2本以上的上书

    rd.hset('qdArt',uid,aid)

    return '抢读成功！'


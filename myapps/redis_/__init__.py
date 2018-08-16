from redis import Redis

rd = Redis('127.0.0.1',db=12)   #创建Redis对象

def incrTopRank(id):
    #自增id的阅读排行
    rd.zincrby('ReadTopRank',id)


def getReadTopRank(top):
    #获取排名前top的文章
    topRanks = rd.zrevrange('ReadTopRank',0,top-1,withscores=True)  #[(b'1',10),...]

    try:
        from art.models import Art
        # topArts_ = Art.objects.in_bulk([int(id_.decode()) for id_,_ in topRanks])
        return [(Art.objects.get(pk=int(id_.decode())), int(score)) for id_, score in topRanks]
    except:
        pass





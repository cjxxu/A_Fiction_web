from django.http import JsonResponse
from django.shortcuts import render
from redis_ import rd
# Create your views here.
from django.views.decorators.cache import cache_page

from art.models import Art
from user import helper
import redis_
from art import tasks

@cache_page(30)
def show(request,id):
    login_user = helper.getLoginInfo(request)  #读取session登陆信息
    #阅读art_id的文章
    art = Art.objects.get(pk=id)

    #写入到阅读排行中（Redis->ReadTopRank）
    redis_.incrTopRank(id)

    readTopRank = redis_.getReadTopRank(5)  #[(,score)]

    return render(request,'art/show.html',locals())

def qdArt(request,id):
    #获取当前登录的用户信息
    login_user = helper.getLoginInfo(request)
    if not login_user:
        return JsonResponse({'msg':'请先登录','code':101})

    tasks.qdTask.delay(login_user.get(id),id)  #延迟异步执行
    return JsonResponse({'msg':'正在抢读','code':201})

def queryQDState(request,id):
    login_user = helper.getLoginInfo(request)
    if not login_user:
        return JsonResponse({'msg':'请先登录','code':101})

    uid = login_user.get('id')
    # if rd.hexists('qdArt',uid):
    #     # 一个用户抢两本书，查询最新的id的抢读状态，而不是之前抢读的状态
    #     qdId = rd.hget('qdArt', uid)  # 已抢的书id,  qdId和id可能不一样

    if login_user.get('id'):
        art = Art.objects.get(pk=id)
        return JsonResponse({'msg':'抢读成功','code':200,
                             'art':{'title':art.title,
                                    'author':art.author}
                             })
    if rd.hlen('qdArt') < 5:
        return JsonResponse({'msg': '抢读中', 'code': 201})
    else:
        return JsonResponse({'msg': '抢读失败', 'code': 300})

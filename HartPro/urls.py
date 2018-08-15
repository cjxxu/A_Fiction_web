"""HartPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.core.paginator import Paginator
from django.shortcuts import render
from art.models import Tag,Art

import xadmin as admin

def toIndex(request):
    tags1 = Tag.objects.all()
    # locals将当前函数的局部变量转成字典的key-value结构
    #{'request':request,'tags':tags}
    tags = []
    for tag in tags1:
        #判断该类型中是否有文章,如果有就添加进tags
        if Art.objects.filter(tag=tag):
            tags.append(tag)
    #annotate为每个tag对象增加一个字段(Count('art) 统计每种类型下文章数据)
    #
    #读取分类id
    tag_id = request.GET.get('tag')
    if tag_id:
        tag_id = int(tag_id)
        arts = Art.objects.filter(tag_id=tag_id)  #exclude排除条件为真的数据
    else:
        arts = Art.objects.all()

    # #加载所有文章
    # arts = Art.objects.all()

    #将文章进行分页处理
    paginator = Paginator(arts,8)   #分页器

    page = request.GET.get('page')
    page = int(page) if page else 1  # 读取请求参数中page参数，如果没有,默认为1
    pager = paginator.page(page)  # 获取当前页的数据

    return render(request,'index.html',locals())


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^user/',include('user.urls')),
    url(r'^$', toIndex),
]



from __future__ import absolute_import
import os
from celery import Celery
from HartPro import settings

#设置环境变量
os.environ.setdefault('DJANGO_SETTINGS_MODULE','HartPro.settings')


#创建Celey对象
app = Celery('hart')

#加载配置
app.config_from_object('django.conf:settings')

#自动发现task异步任务
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
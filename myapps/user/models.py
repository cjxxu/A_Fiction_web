from django.contrib.auth.hashers import make_password
from django.db import models

# Create your models here.

class UserProfile(models.Model):
    username = models.CharField(max_length=20,unique=True,verbose_name='用户名')
    passwd = models.CharField(max_length=100,verbose_name='口令')
    email = models.CharField(max_length=50,unique=True,verbose_name='邮箱')
    photo = models.CharField(max_length=100,verbose_name='头像',blank=True,null=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        # 修改用户邮箱时,口令没有改变的情况下,如何避免重复加密
        self.passwd = make_password(self.passwd)  #加密
        super().save()


    class Meta:
        db_table = 't_user'
        verbose_name = '客户'
        verbose_name_plural = verbose_name
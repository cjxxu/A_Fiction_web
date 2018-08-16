from django import forms
from django.core.exceptions import ValidationError

from user.models import UserProfile


class UserForm(forms.ModelForm):
    username = forms.CharField(min_length=8,max_length=20,
                               error_messages={
                                   'required': '用户名不能为空',
                                   'max_length': '用户名超出了20个字符',
                                   'min_length': '用户名的长度不能低于8位'
                               })
    passwd2 = forms.CharField(min_length=8,required=True,
                              error_messages={
                                  'required': '重复口令不能为空',
                                  'min_length': '用户名的长度不能低于8位'
                              })

    class Meta:
        model = UserProfile
        fields = '__all__'
        error_messages = {
            'passwd':{
               'required':'口令不能为空'
            },
            'email':{
                'required':'邮箱不能为空'
            }
        }


    #通过clean_xxx字段名,实现除了required,min,max之外的验证
    #如果验证不通过,可以通过 ValidationError向errors中添加错误
    def clean_passwd2(self):
        #cleaned_data  去除了字段中两边的空白
        p1 = self.cleaned_data.get('passwd')
        p2 = self.cleaned_data.get('passwd2')

        if p1 is not None and p1 == p2:
            return p1
        raise ValidationError('两次口令不相同')
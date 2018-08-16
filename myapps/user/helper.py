import json

def getLoginInfo(request)->dict:
    '''
    获取当前登录用户的信息
    :param request: 请求对象
    :return: 返回None或{''}
    '''
    login_user = request.session.get('login_user')
    if login_user:
        login_user = json.loads(login_user)  #将json字符串转为字典对象

    return login_user

def addLoginSession(request,user):
    request.session['login_user'] = json.dumps({'id': user.id,
                                                'name': user.username,
                                                'photo': user.photo})
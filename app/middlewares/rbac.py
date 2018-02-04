# 在该文件中，实现检查用户权限，控制访问。

import re
from django.conf import settings
from django.shortcuts import render,redirect,HttpResponse

class MiddlewareMixin(object):
    def __init__(self,get_response=None):
        self.get_response = get_response
        super(MiddlewareMixin, self).__init__()
    def __call__(self, request): # 在实例化时候会自动调用它
        response = None
        if hasattr(self,'process_request'):
            response = self.process_request(request)
        if not response:
            response = self.get_response(request)
        if hasattr(self,'process_response'):
            response = self.process_response(request,response)
        return response


class RbacMiddleware(MiddlewareMixin):
    """
    第一步：请求开始之初，先判断一下白名单。
    第二步：拿到当前登录用户的所有权限
    第三步：
    """
    def process_request(self,request):
        current_url = request.path_info
        for url in settings.WHITE_URLS:
            # 如果当前请求的url是在白名单里面的话。就过
            if re.match(url,current_url):
                return
        # 拿到当前用户的所有权限
        permission_dict = request.session.get(settings.PERMISSION_URL_KEY)
        if not permission_dict:
            return  redirect('/login')

        flag = False
        for group_id,codes_urls in permission_dict.items():
            # print(permission_dict.items())
            # dict_items([('2', {'codes': ['list', 'add'], 'urls': ['/order/', '/order/add/']})])
            for permission_url in codes_urls['urls']:
                # permission_url== /order/
                # permission_url== /order/add/
                regex = '^{0}$'.format(permission_url)
                # line-42regex=== ^/order/$
                # line-42regex=== ^/order/add/$
                # 这步的意义权当是给你当前匹配到的url，加上起始和终止符。
                if re.match(regex,current_url):
                    request.permission_code_url = codes_urls['code']
                    # 匹配成功之后，写进request中，方便判断
                    flag  = True
                    break
                if flag :
                    break
            if not flag:
                return HttpResponse('sorry,您无权访问！！！要想访问，先充会员🌚####无法换行')

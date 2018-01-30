from django.conf import settings
from collections import defaultdict
def init_permission(request,user):
    """
    用户在登录成功后，会获取用户的权限信息，并且将其保存在session中。
    初始化权限信息，并写入到session中。
    :param user: 当前登录成功的用户
    :param request:
    :return:
    """
    current_url = request.path_info  # 获取当前请求的url
    # print(current_url)
    permission_list = user.role.values('permission__id',             # 为什么__id， 因为是多对多，它必须杠杠呀。不然找不到的。
                                       'permission__code',           # 权限别名：list,edit,del,add
                                       'permission__name',           # 权限名称: 用户列表，订单列表，编辑用户，编辑订单...前端菜单显示用。
                                       'permission__url',            # 权限对应的url
                                       'permission__menu_group_id',  # 所属菜单组ID，内关联的permission
                                       'permission__permission_group_id',          # 所属权限组id
                                       'permission__permission_group__name',       # 所属权限组的名称
                                       'permission__permission_group__menu_id',    # 所属权限组的菜单id
                                       'permission__permission_group__menu__name'  # 菜单名
                                       ).distinct()   # 去重
    # print(permission_list)
    """
    permission_list < QuerySet[{'permission__id': 1, 'permission__code': 'list', 'permission__url': '/userinfo/',
                                'permission__menu_group_id': None, 'permission__permission_group_id': 1,
                                'permission__permission_group__name': '用户组', 'permission__permission_group__menu_id': 1,
                                'permission__permission_group__menu__name': '菜单一'}, {'permission__id': 5,
                                                                                     'permission__code': 'list',
                                                                                     'permission__url': '/order/',
                                                                                     'permission__menu_group_id': None,
                                                                                     'permission__permission_group_id': 2,
                                                                                     'permission__permission_group__name': '订单组',
                                                                                     'permission__permission_group__menu_id': 2,
                                                                                     'permission__permission_group__menu__name': '菜单二'}, {
                                   'permission__id': 6, 'permission__code': 'add', 'permission__url': '/order/add/',
                                   'permission__menu_group_id': 5, 'permission__permission_group_id': 2,
                                   'permission__permission_group__name': '订单组',
                                   'permission__permission_group__menu_id': 2,
                                   'permission__permission_group__menu__name': '菜单二'}] >
    """

    # 权限相关
    """
    permission_url_dict数据结构如下
    {
        1: {
            'codes': ['list', 'add', 'edit', 'del'], 
            'urls': ['/userinfo/', '/userinfo/add/', '/userinfo/edit/(\\d+)/', '/userinfo/del/(\\d+)/']
        },
        2: {
            'codes': ['list', 'add', 'edit', 'del'], 
            'urls': ['/order/', '/order/add/', '/order/edit/(\\d+)/', '/order/del/(\\d+)/']
        }
    }
    """
    p_url_dict = {}
    for item in permission_list:
        group_id = item['permission__permission_group_id']
        url = item['permission__url']
        # menu_group_id = item['permission__permission_group__menu_id']
        code = item['permission__code']
        if group_id in p_url_dict:
            p_url_dict[group_id]['codes'].append(code)
            p_url_dict[group_id]['urls'].append(url)
        else:
            p_url_dict[group_id] = {'codes':[code,],'urls':[url,]}
    request.session[settings.PERMISSION_URL_KEY] = p_url_dict  # 将用户的权限信息保存在session中。

    # 菜单相关
    """
    permission_menu_list 数据结构如下
    [
        {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单一'}, 
        {'id': 2, 'title': '添加用户', 'url': '/userinfo/add/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'}, 
        {'id': 3, 'title': '编辑用户', 'url': '/userinfo/edit/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单一'}, 
        {'id': 4, 'title': '删除用户', 'url': '/userinfo/del/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title':'菜单一'}, 
        {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单二'}, 
        {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'},
        {'id': 7, 'title': '编辑订单', 'url': '/order/edit/(\\d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}, 
        {'id': 8, 'title': '删除订单', 'url': '/order/del/(\\d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}
    ]
    """
    permission_menu_list = []
    for item in permission_list:
        tpl = {
            'id':item['permission__id'],
            'title':item['permission__name'],
            'url':item['permission__url'],
            'menu_group_id':item['permission__menu_group_id'],
            'menu_id':item['permission__permission_group_id'],
            'menu_title':item['permission__permission_group__menu__name']
        }
        permission_menu_list.append(tpl)
    request.session[settings.PERMISSION_MENU_KEY] = permission_menu_list   # 将用户的菜单信息保存到session中。

"""
# print(item)  登录用户： pp 
{'permission__id': 1, 'permission__code': 'list', 'permission__name': '用户列表', 'permission__url': '/userinfo/', 'permission__menu_group_id': None, 'permission__permission_group_id': 1, 'permission__permission_group__name': '用户组', 'permission__permission_group__menu_id': 1, 'permission__permission_group__menu__name': '菜单一'}
{'permission__id': 5, 'permission__code': 'list', 'permission__name': '订单列表', 'permission__url': '/order/', 'permission__menu_group_id': None, 'permission__permission_group_id': 2, 'permission__permission_group__name': '订单组', 'permission__permission_group__menu_id': 2, 'permission__permission_group__menu__name': '菜单二'}
{'permission__id': 6, 'permission__code': 'add', 'permission__name': '添加订单', 'permission__url': '/order/add/', 'permission__menu_group_id': 5, 'permission__permission_group_id': 2, 'permission__permission_group__name': '订单组', 'permission__permission_group__menu_id': 2, 'permission__permission_group__menu__name': '菜单二'}

# print('PERMISSION_URL_KEY===>',request.session.get(settings.PERMISSION_URL_KEY))
PERMISSION_URL_KEY===> {1: {'codes': ['list'], 'urls': ['/userinfo/']}, 2: {'codes': ['list', 'add'], 'urls': ['/order/', '/order/add/']}}

# print('PERMISSION_MENU_KEY==>',request.session.get(settings.PERMISSION_MENU_KEY))
PERMISSION_MENU_KEY==> [{'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_group_id': None, 'menu_id': 1, 'menu_title': '菜单一'}, {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_group_id': None, 'menu_id': 2, 'menu_title': '菜单二'}, {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_group_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}]
"""
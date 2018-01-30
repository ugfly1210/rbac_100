from django.test import TestCase

# Create your tests here.

from app import models

# models.User.objects.create(username='gay⑥日华',password=123)
# models.User.objects.create(username='🌞阳勇',password=123)
# models.User.objects.create(username='李龙儿🐲',password=123)
# models.User.objects.create(username='pp',password=123)
# models.User.objects.create(username='ff',password=123)
#
# models.Role.objects.create(name='CEO')
# models.Role.objects.create(name='总监')
# models.Role.objects.create(name='经理')
# models.Role.objects.create(name='业务员')
#
# models.Menu.objects.create(name='菜单一')
# models.Menu.objects.create(name='菜单二')
# models.PermissionGroup.objects.create(name='用户组',menu_id=1)
# models.PermissionGroup.objects.create(name='订单组',menu_id=2)
#
# models.Permission.objects.create(name='用户列表',url='/userinfo/',code='list',permission_group_id=1,menu_group_id=None)
# models.Permission.objects.create(name='添加用户',url='/userinfo/add/',code='add',permission_group_id=1,menu_group_id=1)
# models.Permission.objects.create(name='编辑用户',url='/userinfo/edit/(\d+)',code='edit',permission_group_id=1,menu_group_id=1)
# models.Permission.objects.create(name='删除用户',url='/userinfo/del/(\d+)',code='del',permission_group_id=1,menu_group_id=1)
#
# models.Permission.objects.create(name='订单列表',url='/order/',code='list',permission_group_id=2,menu_group_id=None)
# models.Permission.objects.create(name='添加订单',url='/order/add/',code='add',permission_group_id=2,menu_group_id=5)
# models.Permission.objects.create(name='编辑订单',url='/order/edit/(\d+)',code='edit',permission_group_id=2,menu_group_id=5)
# models.Permission.objects.create(name='删除订单',url='/order/del/(\d+)',code='del',permission_group_id=2,menu_group_id=5)
#
#
# models.User.objects.get(username='gay⑥日华').role.add(1)
# models.User.objects.get(username='🌞阳勇').role.add(2)
# models.User.objects.get(username='李龙儿🐲').role.add(3)
# models.User.objects.get(username='pp').role.add(3,4)
# models.User.objects.get(username='ff').role.add(4)
#
# models.Role.objects.get(name='CEO').permission.add(1,2,3,4,5,6,7,8)
# models.Role.objects.get(name='总监').permission.add(1,2,5,6)
# models.Role.objects.get(name='经理').permission.add(1,5)
# models.Role.objects.get(name='业务员').permission.add(5,6)



"""
{'permission__id': 1, 'permission__code': 'list', 'permission__name': '用户列表', 'permission__url': '/userinfo/', 'permission__menu_group_id': None, 'permission__permission_group_id': 1, 'permission__permission_group__name': '用户组', 'permission__permission_group__menu_id': 1, 'permission__permission_group__menu__name': '菜单一'}
{'permission__id': 5, 'permission__code': 'list', 'permission__name': '订单列表', 'permission__url': '/order/', 'permission__menu_group_id': None, 'permission__permission_group_id': 2, 'permission__permission_group__name': '订单组', 'permission__permission_group__menu_id': 2, 'permission__permission_group__menu__name': '菜单二'}
{'permission__id': 6, 'permission__code': 'add', 'permission__name': '添加订单', 'permission__url': '/order/add/', 'permission__menu_group_id': 5, 'permission__permission_group_id': 2, 'permission__permission_group__name': '订单组', 'permission__permission_group__menu_id': 2, 'permission__permission_group__menu__name': '菜单二'}
PERMISSION_URL_KEY===> {1: {'codes': ['list'], 'urls': ['/userinfo/']}, 2: {'codes': ['list', 'add'], 'urls': ['/order/', '/order/add/']}}
PERMISSION_MENU_KEY==> [{'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_group_id': None, 'menu_id': 1, 'menu_title': '菜单一'}, {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_group_id': None, 'menu_id': 2, 'menu_title': '菜单二'}, {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_group_id': 5, 'menu_id': 2, 'menu_title': '菜单二'}]
"""

from app import models
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.

def test(request):
    models.User.objects.create(username='gay⑥日华',password=123)
    models.User.objects.create(username='🌞阳勇',password=123)
    models.User.objects.create(username='李龙儿🐲',password=123)
    models.User.objects.create(username='pp',password=123)
    models.User.objects.create(username='ff',password=123)

    models.Role.objects.create(name='CEO')
    models.Role.objects.create(name='总监')
    models.Role.objects.create(name='经理')
    models.Role.objects.create(name='业务员')

    models.Menu.objects.create(name='菜单一')
    models.Menu.objects.create(name='菜单二')
    print('6666666666666')
    models.PermissionGroup.objects.create(name='用户组',menu_id=1)
    models.PermissionGroup.objects.create(name='订单组',menu_id=2)

    models.Permission.objects.create(name='用户列表',url='/userinfo/',code='list',permission_group_id=1,menu_group_id=None)
    models.Permission.objects.create(name='添加用户',url='/userinfo/add/',code='add',permission_group_id=1,menu_group_id=1)
    models.Permission.objects.create(name='编辑用户',url='/userinfo/edit/(\d+)',code='edit',permission_group_id=1,menu_group_id=1)
    models.Permission.objects.create(name='删除用户',url='/userinfo/del/(\d+)',code='del',permission_group_id=1,menu_group_id=1)

    models.Permission.objects.create(name='订单列表',url='/order/',code='list',permission_group_id=2,menu_group_id=None)
    models.Permission.objects.create(name='添加订单',url='/order/add/',code='add',permission_group_id=2,menu_group_id=5)
    models.Permission.objects.create(name='编辑订单',url='/order/edit/(\d+)',code='edit',permission_group_id=2,menu_group_id=5)
    models.Permission.objects.create(name='删除订单',url='/order/del/(\d+)',code='del',permission_group_id=2,menu_group_id=5)


    models.User.objects.get(username='gay⑥日华').role.add(1)
    models.User.objects.get(username='🌞阳勇').role.add(2)
    models.User.objects.get(username='李龙儿🐲').role.add(3)
    models.User.objects.get(username='pp').role.add(3,4)
    models.User.objects.get(username='ff').role.add(4)

    models.Role.objects.get(name='CEO').permission.add(1,2,3,4,5,6,7,8)
    models.Role.objects.get(name='总监').permission.add(1,2,5,6)
    models.Role.objects.get(name='经理').permission.add(1,5)
    models.Role.objects.get(name='业务员').permission.add(5,6)
    return HttpResponse('6666666666')


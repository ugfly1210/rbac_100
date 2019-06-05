# Rbac
## 1. 先创建项目

```
rbac
```

## 2. 在settings中配置

```
INSTALL_APPS DATABASES STATICFILES_DIRS
```

## 3. 设计表

```python
五个类，七张表 (之前做过...)
User,Role,Permission,Menu,PermissionGroup
User：用来存储注册的用户信息。
Role：角色扮演。一个用户可以拥有多个角色，一个角色也可以分配给多个用户。M2M
Permission：权限相关。给角色分配的权限。M2M
PermissionGroup：多个权限附属在一个权限组下。权限和权限组多对一。
Menu：一个菜单下面包含多个权限组。菜单和权限组一对多。
```

别慌，还早。夜还长。

##### 菜单表存在的意义：

    
    菜单
    它为什么要存在？
    你这样想，你在前端页面展示的时候，如果你现在需要编辑功能，你点击编辑之后，
    因为你的编辑不是菜单选项，你的菜单栏是不是就没啦？ 对不对
    所以， 我们需要规定一下哪些可以是菜单，并且可以被默认选中。并且要把默认选中的菜单与菜单一关联起来。

    再深入一点好不好
    来，这样想。
    权限方面我们就实现add,del,edit,还有一个查。
    一个菜单下面如果只能包含一个菜单组的东西是不是太寡了。
    比如：我有订单组和人事管理组，订单组里面分为增删改查，人事管理有增删改查。
        可不可以实现在菜单一下面显示订单管理和人事管理？
        对，就按照这个路子来。人间正道就是野路子。
    

**另外**：一个权限下也可能有多个权限子菜单，也可能有一个权限父菜单：权限和权限是自引用关系。这里可能有点绕。 你这样理解，因为我们要有一个权限来作为显示菜单，对照下面代码：

menu_gp_id为None的，就是菜单。你不可能把编辑和增加或者删除也列到菜单里面去吧。这两或三个功能应该是在你详情页里面。

```python
menu_list = [
    {'id': 1, 'title': '用户列表', 'url': '/userinfo/', 'menu_gp_id': None, 'menu_id': 1, 'menu_title': '菜单管理'},
    {'id': 2, 'title': '添加用户', 'url': '/userinfo/add/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单管理'},
    {'id': 3, 'title': '删除用户', 'url': '/userinfo/del/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单管理'},
    {'id': 4, 'title': '修改用户', 'url': '/userinfo/edit/(\\d+)/', 'menu_gp_id': 1, 'menu_id': 1, 'menu_title': '菜单管理'},

    {'id': 5, 'title': '订单列表', 'url': '/order/', 'menu_gp_id': None, 'menu_id': 2, 'menu_title': '菜单2'},
    {'id': 6, 'title': '添加订单', 'url': '/order/add/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单2'},
    {'id': 7, 'title': '删除订单', 'url': '/order/del/(\\d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单2'},
    {'id': 8, 'title': '修改订单', 'url': '/order/edit/(\\d+)/', 'menu_gp_id': 5, 'menu_id': 2, 'menu_title': '菜单2'}
]

menu_dict = {}
for item in menu_list:
    if not item['menu_gp_id']:
        menu_dict[item['id']] = item

menu_list[0]['active'] = True

print(menu_dict)
```

## 4. 关于数据插入

```python
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

```

#### 关于多对多的插入：

​	因为多对多会产生第三张表，django的orm里是找不到这张表的。你必须自己手动去插入。要么就是使用数据库，直接操作第三张表。

​	django ORM里面的多对多插入方法：点关联字段然后add   完事。



## 5. init_permission:关于用户成功登录后，拿到用户的权限信息以及菜单信息。

```python
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
```

# 6. 编写RbacMiddleware
  首先在settings里面注册中间件
  ```
      'app.middlewares.rbac.RbacMiddleware',
  ```
  ### 编写流程
  ```
  然后第一步：
    判断当前申请访问的url是否白名单
    从session中获取当前登录用户的permission_dict
  第二步:
    遍历你的permission_dict
    给url加上起始终止符
    并且写入你的request
    code对应url
    end
```

from django.db import models

# Create your models here.

class User(models.Model):
    """
    用户表
    """
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=32,verbose_name='密码')
    role = models.ManyToManyField(to='Role',verbose_name='与角色多对多绑定')
    def __str__(self):
        return self.username


class Role(models.Model):
    """
    角色
    """
    name = models.CharField(max_length=32,verbose_name='角色名称')
    permission = models.ManyToManyField(to='Permission',verbose_name='与权限多对多绑定')
    def __str__(self):
        return  self.name

class Permission(models.Model):
    """
    权限表
    """
    name = models.CharField(max_length=32,verbose_name='权限名称')
    url = models.CharField(max_length=32,verbose_name='权限对应路径')
    code = models.CharField(max_length=32,verbose_name='权限别称')

    menu_group = models.ForeignKey(to='Permission',verbose_name='所属菜单组',related_name='iloveu',default=None,null=True)
    permission_group = models.ForeignKey(to='PermissionGroup',verbose_name='所属权限组',)
    def __str__(self):
        return self.name

class PermissionGroup(models.Model):
    """
    权限分组
    """
    name = models.CharField(max_length=32,verbose_name='权限组名称')
    menu = models.ForeignKey(to='Menu',verbose_name='当前权限分组所属菜单')
    def __str__(self):
        return self.name

class Menu(models.Model):
    """
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
    """
    name = models.CharField(max_length=32,verbose_name='菜单名称')
    def __str__(self):
        return self.name

"""
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
"""

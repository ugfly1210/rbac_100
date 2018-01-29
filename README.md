# rbac_100
###第一次提交，表结构设计思路。
1. 先创建项目

    rbac

2. 在settings中配置

    INSTALL_APPS DATABASES STATICFILES_DIRS

3. 设计表

    五个类，七张表 (之前做过...)
    User,Role,Permission,Menu,PermissionGroup
    User：用来存储注册的用户信息。
    Role：角色扮演。一个用户可以拥有多个角色，一个角色也可以分配给多个用户。M2M
    Permission：权限相关。给角色分配的权限。M2M
    PermissionGroup：多个权限附属在一个权限组下。权限和权限组多对一。
    Menu：一个菜单下面包含多个权限组。菜单和权限组一对多。

别慌，还早。夜还长。

菜单表存在的意义：

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

另外：一个权限下也可能有多个权限子菜单，也可能有一个权限父菜单：权限和权限是自引用关系。这里可能有点绕。 你这样理解，因为我们要有一个权限来作为显示菜单，对照下面代码：

menu_gp_id为None的，就是菜单。你不可能把编辑和增加或者删除也列到菜单里面去吧。这两或三个功能应该是在你详情页里面。

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

关于多对多的插入：

	因为多对多会产生第三张表，django的orm里是找不到这张表的。你必须自己手动去插入。要么就是使用数据库，直接操作第三张表。

	django ORM里面的多对多插入方法：点关联字段然后add   完事。


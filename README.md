# connect_mysql
mysql简单封装
    '''
    insert_obj = {
        # 增加  ,select和where可为空
        'id': 111,
        'order': 111,
        'order_id': 111,
        'rate_star': 111,
    },
    
    delete_obj = {
        # 删除    select 可省去
        # 删除条件字段
        'order_id': 111,
        'rate_star': 111,
        'where_list': ['order_id', 'rate_star']
    },
    
    update_obj = {
        # 更新  select可省去，
        # 待更新字段
        'order_id': 60263167670871,
        ...
        'id': 60263167670871,
        # 条件字段
        'rate_star': 1111,
        'order_id': 60263167670871,
        'where_list': ['order_id', 'rate_star']
    },
    
    select_obj = {
        # 查询

        # 条件字段
        'order_id': 111,
        'rate_star': 111,
        'where_list': ['order_id', 'rate_star'],

        # 待查询字段
        'select_list': ['id', 'star']
    }        
    '''

# *coding:utf-8 *
import json
import pymysql


class db_settings:
    '''
    例：
    db_obj = {
        'field1': 'field1',
        'field2': 'field2',
        'where_field1':'where_field1',
        'where_field2':'where_field1',
        'select_list': ['select_field1', 'select_field2'],  # select查询字段
        'where_list': ['where_field1', 'where_field2']  # where条件字段
    }
    '''

    def __init__(self, db=None, user=None, password=None, host='localhost', port=3306, charset='utf8'):
        self.conn_mysql = pymysql.Connect(
            database=db,
            user=user,
            password=password,
            host=host,
            port=port,
            charset=charset,
        )


    def __del__(self):
        self.conn_mysql.close()

    def db_selete(self, *args, **kwargs):
        # 获取数据字段
        # 整理出sql
        # 调用db
        table = args[0]
        where_fields = ''
        data = kwargs.get('data')
        where_list = data.get('where_list')
        select_list = data.get('select_list')
        if where_list !=None:
            del data['where_list']
        if select_list != None:
            del data['select_list']
        for k, v in data.items():
            if k in where_list:
                if where_fields == '':
                    where_fields += f"{k}='{v}'"
                else:
                    where_fields += f"and {k}='{v}'"
        fields = ','.join(select_list)

        cursor = self.conn_mysql.cursor()
        sql = f"""select {fields} from {table} where {where_fields}"""
        cursor.execute(sql)
        result = cursor.fetchall()
        return result

    def db_update(self, *args, **kwargs):
        table = args[0]
        fields = ''
        where_fields = ''
        data = kwargs.get('data')
        where_list = data.get('where_list')
        select_list = data.get('select_list')
        if where_list != None:
            del data['where_list']
        if select_list != None:
            del data['select_list']
        for k, v in data.items():
            if k in where_list:
                if where_fields == '':
                    where_fields += f"{k}='{v}'"
                else:
                    where_fields += f"and {k}='{v}'"
            else:
                if fields == '':
                    fields += f"{k}='{v}'"
                else:
                    fields += f", {k}='{v}'"

        # 调用sql
        cursor = self.conn_mysql.cursor()
        sql = f"""update {table} set {fields} where {where_fields}"""
        try:
            cursor.execute(sql)
            self.conn_mysql.commit()
        except Exception as e:
            print(e)
            self.conn_mysql.rollback()

    def db_insert(self, *args, **kwargs):
        table = args[0]
        fields = ''
        where_fields = ''
        data = kwargs.get('data')
        where_list = data.get('where_list')
        select_list = data.get('select_list')
        if where_list != None:
            del data['where_list']
        if select_list != None:
            del data['select_list']
        num = 0
        for k, v in data.items():
            if num == 0:
                where_fields += f"{k}"
                fields += f"'{v}'"
            else:
                where_fields += f", {k}"
                fields += f", '{v}'"
            num += 1

        cursor = self.conn_mysql.cursor()
        sql = f"""insert into {table} ({where_fields}) values({fields})"""
        try:
            cursor.execute(sql)
            self.conn_mysql.commit()
        except Exception as e:
            print(e)
            self.conn_mysql.rollback()

    def db_delete(self, *args, **kwargs):
        table = args[0]
        fields = ''
        where_fields = ''
        data = kwargs.get('data')
        where_list = data.get('where_list')
        select_list = data.get('select_list')
        if where_list != None:
            del data['where_list']
        if select_list != None:
            del data['select_list']
        for k, v in data.items():
            if fields == '':
                fields += f"{k}='{v}'"
            else:
                fields += f", {k}='{v}'"
            if k in where_list:
                if where_fields == '':
                    where_fields += f"{k}='{v}'"
                else:
                    where_fields += f"and {k}='{v}'"

        cursor = self.conn_mysql.cursor()
        sql = f"""delete from {table} where {where_fields}"""
        try:
            cursor.execute(sql)
            self.conn_mysql.commit()
        except Exception as e:
            print(e)
            self.conn_mysql.rollback()


if __name__ == '__main__':

    # 操作
    local_class = db_settings(db='db', user='root', password='123', host='host')
    localize_update_obj = {
        # 查询
        # 查询条件字段
        'order_id': 111,
        'rate_star': 111,
        'where_list': ['order_id', 'rate_star'],
        # 查询字段
        'select_list': ['id', 'star']
    }
    local_class.db_selete('shopee_customer', data=localize_update_obj)

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
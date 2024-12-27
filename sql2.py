import pymysql


def getmysql(sql):
    # 数据库连接参数-测试环境base
    config = {
        'host': 'rm-bp106y19fa3992tt9613.mysql.rds.aliyuncs.com',  # 数据库主机地址
        'user': 'tst_tu_bf3b3da',  # 数据库用户名
        'password': 'tst_tu_bf3b3da_447cab',  # 数据库密码
        'database': 'tech_magic_base_00',  # 要连接的数据库名
        'charset': 'utf8',  # 编码方式，根据需要设置
        'cursorclass': pymysql.cursors.DictCursor  # 返回的查询结果是字典格式
    }

    # 创建数据库连接
    connection = pymysql.connect(**config)

    try:
        # 使用连接创建游标对象
        with connection.cursor() as cursor:
            # 执行SQL查询
            cursor.execute(sql)
            # 获取所有查询结果
            results = cursor.fetchall()
            i = 0
            for row in results:
                print(row)
                i = i+1
            print(f"总共查到{i}条记录")
    finally:
        # 关闭数据库连接
        connection.close()


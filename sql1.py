import psycopg2
from psycopg2.extras import DictCursor


def getpgsql(sql):
    # 数据库连接参数-测试环境base
    connection = psycopg2.connect(
        user="postgres",
        password="Cubeinfo_2024",
        host="172.28.38.22",  # 或你的数据库服务器地址
        port="5432",  # PostgreSQL默认端口
        database="mantis"
    )

    try:
        # 使用连接创建游标对象
        with connection.cursor(cursor_factory=DictCursor) as cursor:
            # 执行SQL查询
            cursor.execute(sql)
            # 获取所有查询结果
            results = cursor.fetchall()
            i = 0
            for row in results:
                print(row)
                i = i + 1
            print(f"总共查到{i}条记录")
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        # 关闭数据库连接
        connection.close()
    return results


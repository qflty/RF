import pymysql

from position.constants import my_test_host, my_test_port, my_test_user, my_test_password, my_test_database


class MysqlManager:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """连接数据库"""
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database,
                                   cursorclass=pymysql.cursors.DictCursor)
            cursor = conn.cursor()
            return cursor
        except Exception as e:
            print(f"数据库连接失败:{e}")

    def get_data(self, sql):
        global cursor
        try:
            cursor = self.connect()
            cursor.execute(sql)
            return cursor.fetchone()
        except:
            print('数据库操作失败，请检查！')
        finally:
            cursor.close()

    def get_all_data(self, sql):
        try:
            # 使用连接创建游标对象
            cursor = self.connect()
            # 执行SQL查询
            cursor.execute(sql)
            # 获取所有查询结果
            results = cursor.fetchall()
            i = 0
            for row in results:
                print(row)
                i = i + 1
            print(f"总共查到{i}条记录")
            return results
        except (Exception, pymysql.Error) as error:
            print("数据库操作失败:", error)
        finally:
            cursor.close()


# if __name__ == "__main__":
#     host = my_test_host
#     port = my_test_port
#     user = my_test_user
#     password = my_test_password
#     database = my_test_database
#     mysql = MysqlManager(host, port, user, password, database)
#     sql_query = "select * from mars_case_library where space_id = 8143 and is_deleted = 'N' order by gmt_created;"
#     all_data = MysqlManager.get_all_data(mysql, sql_query)
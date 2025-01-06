import psycopg2
from psycopg2.extras import DictCursor

from position.constants import pg_test_user, pg_test_password, pg_test_host, pg_test_port, pg_test_database


class PgsqlManager:
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        """连接数据库"""
        try:
            conn = psycopg2.connect(host=self.host,
                                    port=self.port,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database)
            cursor = conn.cursor(cursor_factory=DictCursor)
            return cursor
        except Exception as e:
            print(f"连接数据库失败: {e}")
            return None

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

    def get_all_data(self, sql, params=None):
        # 使用连接创建游标对象
        cursor = self.connect()
        try:
            if cursor:
                # 执行SQL查询
                cursor.execute(sql, params)
                # 获取所有查询结果
                results = cursor.fetchall()
                i = 0
                for row in results:
                    print(row)
                    i = i + 1
                print(f"总共查到{i}条记录")
                return results
            else:
                return []
        except (Exception, psycopg2.Error) as error:
            print(f"执行SQL查询时发生错误: {error}")
            return []
        finally:
            if cursor:
                cursor.close()


# if __name__ == '__main__':
#     user = pg_test_user
#     password = pg_test_password
#     host = pg_test_host
#     port = pg_test_port
#     database = pg_test_database
#     pgsql = PgsqlManager(host, port, user, password, database)
#     sql = "select * from neptune_artifact_scan_plan where plan_name = '扫描方案93584758' and is_deleted = 'N'"
#     all_data = PgsqlManager.get_all_data(pgsql, sql)

import pymysql


class MysqlManager(object):
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db

    def connect(self):
        """连接数据库"""
        try:
            conn = pymysql.connect(host=self.host,
                                   port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   db=self.db)
            cursor = conn.cursor()
            return cursor
        except Exception as e:
            print(e)

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
            cursor = self.connect()
            cursor.execute(sql)
            return cursor.fetchall()  # 返回所有匹配的记录
        except Exception as e:
            print('数据库操作失败，请检查！错误信息:', e)
        finally:
            cursor.close()

    def delete_data(self, param):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            sql = 'DELETE from tech_cube_ship_00.ship_scm_user ssu WHERE ssu.username = "%s"' % param
            print(sql)
            cursor.execute(sql, (param,))
            result = conn.commit()
            return result
        except:
            print("操作失败，请检查！")
        # finally:
        #     cursor.close()
        #     conn.close()


if __name__ == "__main__":
    host = 'rm-bp1dp71y66b0r97gj708.mysql.rds.aliyuncs.com'
    port = 3306
    user = 'tc_dev_5e7cf26'
    password = 'tc_dev_5e7cf26_64732e'
    db = 'tech_cube_ship_00'
    # mc = MysqlManager(host, port, user, password, db)
    # r = mc.delete_data("shyt-v1")
    # print(r)
    mysql = MysqlManager(host, port, user, password, db)
    sql_query = "SELECT * FROM tech_cube_ship_00.ship_scm_user;"
    all_data = MysqlManager.get_all_data(mysql, sql_query)
    for record in all_data:
        print(record)

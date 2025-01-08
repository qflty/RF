from position.constants import pg_test_user, pg_test_host, pg_test_password, pg_test_port, pg_test_database, \
    my_test_host, my_test_port, my_test_user, my_test_password, my_test_database
from sql_sample.mysql import MysqlManager
from sql_sample.pgsql import PgsqlManager


# 数据库连接-测试环境
def getpgsql(sql_query, params=None):
    try:
        user = pg_test_user
        password = pg_test_password
        host = pg_test_host
        port = pg_test_port
        database = pg_test_database
        pgsql_connect = PgsqlManager(host, port, user, password, database)
        result = pgsql_connect.get_all_data(sql_query, params)
        if result is not None:
            return result
        else:
            return []
    except Exception as e:
        print(f"在getpgsql函数中发生错误: {e}")
        return []


def getmysql(sql_query, params=None):
    try:
        host = my_test_host
        port = my_test_port
        user = my_test_user
        password = my_test_password
        database = my_test_database
        mysql_connect = MysqlManager(host, port, user, password, database)
        result = MysqlManager.get_all_data(mysql_connect, sql_query)
        if result is not None:
            return result
        else:
            return []
    except Exception as e:
        print(f"在getmysql函数中发生错误: {e}")
        return []


# getpgsql("select * from neptune_artifact_scan_plan where plan_name = '扫描方案93584758' and is_deleted = 'N'")
# getmysql("select * from mars_case_library where space_id = 8143 and is_deleted = 'N' order by gmt_created;")

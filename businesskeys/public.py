import json
import random

from openpyxl.reader.excel import load_workbook
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from position.constants import URL_TEST, USERNAME_LOCATER, USERNAME, PASSWORD_LOCATER, PASSWORD, LOGIN_BUTTON, BUTTON1, \
    BUTTON2
from sql.connect_sql import getpgsql


# 登录页面
def login(driver):
    driver.open(url=URL_TEST)
    try:
        # 输入账号和密码，点击登录
        driver.input(method=By.ID, locator=USERNAME_LOCATER, text=USERNAME)
        driver.input(method=By.ID, locator=PASSWORD_LOCATER, text=PASSWORD)
        driver.click(method=By.ID, locator=LOGIN_BUTTON)
        driver.sleep()
    except (NoSuchElementException, TimeoutError):
        print("Element not found by ID")
    try:
        driver.click(method=By.XPATH, locator=BUTTON1)
        driver.sleep()
    except (NoSuchElementException, TimeoutError):
        driver.locate(method=By.XPATH, locator=BUTTON2)
        driver.refresh()


# 加载Excel文件
def load_test_data(file_path):
    workbook = load_workbook(file_path)
    sheet = workbook.active
    test_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # 跳过标题行
        test_data.append(row)
    return test_data


# 判断方案创建成功
def judge_plan_create(plan_name):
    try:
        sql_template = f"select * from neptune_artifact_scan_plan where plan_name = %s and is_deleted = %s"
        results = getpgsql(sql_template, (plan_name, 'N'))
        if results:  # 检查是否有返回结果
            if results[0]['plan_name'] == plan_name:
                print(f"自动化创建扫描方案成功:{results[0][0]}")
            else:
                print("自动化创建扫描方案失败")
        else:
            print("自动化创建扫描方案失败：未找到该方案")
    except Exception as e:
        print(f"数据库连接失败：{e}")


# 判断方案删除成功
def judge_plan_delete(plan_name=None):
    sql_template = "select * from neptune_artifact_scan_plan where plan_name = %s AND is_deleted = %s"
    results = getpgsql(sql_template, (plan_name, 'Y'))
    try:
        if results:  # 检查是否有返回结果
            if results[0]['plan_name'] == plan_name:
                print(f"自动化删除扫描方案成功: {plan_name}")
            else:
                print("查询结果与预期不符")
            return results
        else:
            print("自动化删除扫描方案失败：未找到该方案")
    except Exception as e:
        print(f"数据库操作失败：{e}")


# 判断方案编辑成功
def judge_plan_edit(plan_name=None, params=None):
    sql_template = "select * from neptune_artifact_scan_plan where plan_name = %s AND is_deleted = %s"
    results = getpgsql(sql_template, (plan_name, 'N'))
    try:
        if results:  # 检查是否有返回结果
            if params in results[0]['white_cve']:
                print(f"自动化编辑扫描方案成功: {plan_name}")
            else:
                print("查询结果与预期不符")
            return results
        else:
            print("自动化编辑扫描方案失败：未找到该方案")
    except Exception as e:
        print(f"数据库操作失败：{e}")


# 判断任务
def judge_task(sql_template, task_name=None):
    results = getpgsql(sql_template,(task_name,))
    try:
        if results:
            if results[0]['task_name'] == task_name:
                print(f"自动化查询扫描任务成功:{task_name}")
            else:
                print("自动化查询扫描任务失败")
            return results
        else:
            print("自动化查询扫描任务失败：未找到该任务")
    except Exception as e:
        print(f"数据库连接失败：{e}")


# 获取固定长度随机数
def get_number(length):
    num = random.randint(10 ** (length - 1), 10 ** length - 1)
    return num


# 保存cookies
def save_cookies(driver):
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as f:
        f.write(json.dumps(cookies))


# 使用cookies
def load_cookies(driver):
    try:
        with open('cookies.json') as f:
            cookies = json.loads(f.read())
        # 遍历字典获取cookies信息进行添加
        for cookie in cookies:
            driver.add_cookie(cookie)
        else:
            # 刷新页面，清除缓存
            driver.reflesh()
    except:
        print("没有可用的cookies信息")

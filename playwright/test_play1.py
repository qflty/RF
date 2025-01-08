from time import sleep
import allure
import openpyxl
import pytest
from position.constants import URL_TEST, USERNAME_LOCATER, PASSWORD_LOCATER, LOGIN_BUTTON, USER_BUTTON, LOGOUT_BUTTON
from playwright.sync_api import sync_playwright


# 读取Excel文件中的数据
def read_excel_data(file_path, sheet_name):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook[sheet_name]
    data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):  # 假设第一行是标题行
        data.append(row)
    return data


# 定义一个浏览器实例的 fixture，其作用范围为整个模块
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False,channel='msedge')  # 以有头模式启动浏览器（可选）
        yield browser
        browser.close()


# 定义一个浏览器页面的 fixture，其作用范围为每个测试函数
@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


@allure.title('登录验证')
# 登录函数
def login(page, username, password):
    with allure.step('步骤1：打开页面'):
        page.goto(URL_TEST)  # 替换为登录URL
        sleep(5)
    with allure.step('步骤2：输入账号和密码'):
        try:
            page.fill(USERNAME_LOCATER, username)
            page.fill(PASSWORD_LOCATER, password)
        except Exception as e:
            print(f"输入账号密码失败，错误信息：{e}")
    with allure.step('步骤3：点击登录按钮'):
        try:
            page.click(LOGIN_BUTTON)
        except Exception as e:
            print(f"点击登录失败，错误信息：{e}")
    with allure.step('步骤4：判断是否登录成功'):
        try:
            sleep(3)
            page.hover(USER_BUTTON)
            print(f"登录成功:{username}")
            page.click(LOGOUT_BUTTON)
            sleep(3)
            # page.waitForSelector(USERNAME_LOCATER)
        except Exception as e:
            print(f"登录失败:{username},错误{e}")
            raise


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')  # 替换为你的Excel文件路径和Sheet名称
)
def test_login(page, username, password):
    login(page, username, password)

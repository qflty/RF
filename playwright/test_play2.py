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
    for row in sheet.iter_rows(min_row=2, values_only=True):  # 第一行是标题行
        data.append(row)
    return data


# 定义一个浏览器实例的 fixture，其作用范围为整个模块
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, channel='msedge')
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
        page.goto(URL_TEST)
    with allure.step('步骤2：输入账号和密码'):
        page.wait_for_selector(USERNAME_LOCATER)
        page.type(USERNAME_LOCATER, str(username))
        page.type(PASSWORD_LOCATER, str(password))
    with allure.step('步骤3：点击登录按钮'):
        page.click(LOGIN_BUTTON)
    with allure.step('步骤4：判断是否登录成功'):
        try:
            page.wait_for_selector(USER_BUTTON)
            page.hover(USER_BUTTON)
            page.wait_for_selector(LOGOUT_BUTTON)
            page.click(LOGOUT_BUTTON)
            page.wait_for_selector(USERNAME_LOCATER)
            return True
        except Exception:
            # allure.attach.text(f"登录失败: {username}, 错误: {e}", name="登录错误")
            return False


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')
)
def test_login(page, username, password):
    assert login(page, username, password), f"登录失败：{username}"


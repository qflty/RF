import json
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
def login(page, username, password):
    with allure.step('步骤1：打开页面'):
        page.goto(URL_TEST)
    with allure.step('步骤2：输入账号和密码'):
        page.wait_for_selector(USERNAME_LOCATER)
        page.fill(USERNAME_LOCATER, str(username))
        page.fill(PASSWORD_LOCATER, str(password))
    with allure.step('步骤3：点击登录按钮'):
        page.click(LOGIN_BUTTON)
    with allure.step('步骤4：判断是否登录成功'):
        try:
            user_button_exists = page.wait_for_selector(USER_BUTTON, timeout=5000)
            if user_button_exists:
                page.hover(USER_BUTTON)
                logout_button_exists = page.wait_for_selector(LOGOUT_BUTTON, timeout=3000)
                if logout_button_exists:
                    page.click(LOGOUT_BUTTON)
                else:
                    raise AssertionError(f"登录后未找到注销按钮: {username}")
            else:
                raise AssertionError(f"登录失败: 未找到用户按钮，用户名: {username}")
        except Exception as e:
            raise AssertionError(f"登录失败: {username}")


# 创建一个名为data的临时目录，并在该目录下创建一个名为test_results.json的文件，用于存放测试相关的数据或结果
@pytest.fixture(scope="session")
def test_results_collector(tmpdir_factory, request):
    # results = defaultdict(lambda: {'success': 0, 'failure': 0})
    results_file = tmpdir_factory.mktemp("data").join("test_results.json")
    # 将 results_file 路径保存到 session 对象上
    request.session.results_file_path = str(results_file)
    results = {'success': 0, 'failure': 0}
    yield results
    with open(results_file, 'w') as f:
        json.dump(dict(results), f, indent=4)
    print(f"\n测试会话结束，结果已保存到 {results_file}")


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')
)
def test_login(page, username, password, test_results_collector):
    try:
        login(page, username, password)
        test_results_collector['success'] += 1
    except AssertionError as e:
        test_results_collector['failure'] += 1
        raise e


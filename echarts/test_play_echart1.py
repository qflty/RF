import json
import allure
import openpyxl
import pytest
from pyecharts.charts import Bar
from pyecharts import options as opts
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
        page.fill(USERNAME_LOCATER, str(username))
        page.fill(PASSWORD_LOCATER, str(password))
    with allure.step('步骤3：点击登录按钮'):
        page.click(LOGIN_BUTTON)
    with allure.step('步骤4：判断是否登录成功'):
        try:
            user_button_exists = page.wait_for_selector(USER_BUTTON, timeout=5000)
            if user_button_exists:
                page.hover(USER_BUTTON)
                page.wait_for_selector(LOGOUT_BUTTON, timeout=3000)
                page.click(LOGOUT_BUTTON)
            else:
                raise AssertionError(f"登录失败: {username}")
        except Exception:
            pytest.fail(f"登录失败: {username}")
            raise AssertionError(f"登录失败: {username}")


# 创建一个名为data的临时目录，并在该目录下创建一个名为test_results.json的文件，用于存放测试相关的数据或结果
@pytest.fixture(scope="session")
def test_results_collector(tmpdir_factory):
    # test_results = defaultdict(lambda: {'success': 0, 'failure': 0})
    results_file = tmpdir_factory.mktemp("data").join("test_results.json")
    results = {'success': 0, 'failure': 0}
    yield results
    with open(results_file, 'w') as f:
        json.dump(dict(results), f, indent=4)
    print(f"测试会话结束，结果已保存到 {results_file}")


# pytest参数化测试
@pytest.mark.parametrize(
    "username,password",
    read_excel_data('test_data.xlsx', 'Sheet1')
)
def test_login(page, username, password, test_results_collector):
    try:
        login(page, username, password)
        test_results_collector[username]['success'] += 1
    except AssertionError:
        test_results_collector[username]['failure'] += 1


def pytest_sessionfinish(session, exitstatus):
    results_file_path = session.config.getoption("--basetemp") / "data" / "test_results.json"
    # 读取并处理结果文件
    with open(results_file_path, 'r') as f:
        results = json.load(f)
    print(f"测试会话结束后的最终结果：{results}")
    success_count = results['success']  # 直接访问字典中的值
    failure_count = results['failure']
    print(f"钩子函数返回：{results}")
    # 创建柱状图
    bar = Bar()
    bar.add_xaxis(['成功', '失败'])
    bar.add_yaxis('测试结果', [success_count, failure_count])
    bar.set_global_opts(title_opts=opts.TitleOpts(title='登录测试结果'))
    # 渲染图表并保存为HTML文件
    bar.render('login_test_results.html')
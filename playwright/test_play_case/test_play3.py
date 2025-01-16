import pytest
import allure
from businesskeys.public import get_number
from playwright.sync_api import sync_playwright
from tools.tool import change_directory, switch_tabs, input_cve_number
from position.constants import USERNAME, PASSWORD, URL_TEST, USERNAME_LOCATER, PASSWORD_LOCATER, LOGIN_BUTTON, \
    CREATE_BUTTON, PLAN_NAME_LOCATER, STE_DEFAULT, PLAN_DESCRIPTION_INPUT, ADD_BUTTON, PLAN_CONFIRM_BUTTON
from testcases.test_login import read_excel_data


# 定义一个浏览器实例的 fixture，其作用范围为整个模块
@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        # 生成浏览器驱动
        browser = p.chromium.launch(headless=False, channel='msedge')
        yield browser
        browser.close()


# 定义一个浏览器页面的 fixture，其作用范围为每个测试函数
@pytest.fixture(scope="function")
def page(browser):
    # 生成浏览器上下文（context）对象
    context = browser.new_context()
    # 生成浏览器页面page
    page = context.new_page()
    yield page
    context.close()


@allure.title('新建制品扫描方案')
def element_role(page, tab, name, description, number, position):
    with allure.step('步骤1、登录devops'):
        page.goto(URL_TEST)
        page.wait_for_selector(USERNAME_LOCATER)
        page.locator(USERNAME_LOCATER).fill(USERNAME)
        page.locator(PASSWORD_LOCATER).fill(PASSWORD)
        page.locator(LOGIN_BUTTON).click()
    with allure.step('步骤2、进入制品扫描'):
        change_directory(page)
    with allure.step('步骤3、选择tab页'):
        switch_tabs(page, tab)
    with allure.step('步骤4、点击创建方案'):
        page.wait_for_selector(CREATE_BUTTON)
        page.click(CREATE_BUTTON)
    with allure.step('步骤5、输入方案名称'):
        page.wait_for_selector(PLAN_NAME_LOCATER)
        scan_plan_name = name + str(get_number(8))
        page.locator(PLAN_NAME_LOCATER).fill(scan_plan_name)
    with allure.step('步骤6、设为默认'):
        page.click(STE_DEFAULT)
    with allure.step('步骤7、输入描述'):
        scan_plan_description = description + str(get_number(8))
        page.locator(PLAN_DESCRIPTION_INPUT).fill(scan_plan_description)
    with allure.step('步骤8、添加漏洞编号'):
        page.click(ADD_BUTTON)
        input_cve_number(page, position, number)
    with allure.step('步骤9、点击确定'):
        page.click(PLAN_CONFIRM_BUTTON)


@pytest.mark.parametrize(
    "tab,name,description,number,position",
    read_excel_data('test_data.xlsx', 'Sheet2')
)
def test_element_role(page, tab, name, description, number, position):
    element_role(page, tab, name, description, number, position)


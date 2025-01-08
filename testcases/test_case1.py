import pytest
import allure
from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, input_cve_number
from position.constants import CREATE_BUTTON, PLAN_NAME_LOCATER, STE_DEFAULT, PLAN_DESCRIPTION_INPUT, ADD_BUTTON, \
    PLAN_CONFIRM_BUTTON
from businesskeys.public import get_number
from testcases.test_login import read_excel_data
from webkeys.webkeys import BrowserController


@allure.title('新建制品扫描方案')
def create_scan_plan(driver, tab, name, description, number, position):
    """
    :param driver:
    :param tab: 制品扫描tab页
    :param name: 方案名称
    :param description: 描述
    :param number: 漏洞编号
    :param position: 编号位置
    """
    with allure.step('步骤1、登录devops'):
        login(driver)
    with allure.step('步骤2、进入制品扫描'):
        change_directory(driver)
    with allure.step('步骤3、选择tab页'):
        switch_tabs(driver, tab)
    with allure.step('步骤4、点击创建方案'):
        driver.click(By.XPATH, CREATE_BUTTON)
    with allure.step('步骤5、输入方案名称'):
        scan_plan_name = name + str(get_number(8))
        driver.input(By.XPATH, PLAN_NAME_LOCATER, scan_plan_name)
    with allure.step('步骤6、设为默认'):
        driver.click(By.XPATH, STE_DEFAULT)
    with allure.step('步骤7、输入描述'):
        scan_plan_description = description + str(get_number(8))
        driver.input(By.XPATH, PLAN_DESCRIPTION_INPUT, scan_plan_description)
    with allure.step('步骤8、添加漏洞编号'):
        driver.click(By.XPATH, ADD_BUTTON)
        input_cve_number(driver, position, number)
    with allure.step('步骤9、点击确定'):
        driver.click(By.XPATH, PLAN_CONFIRM_BUTTON)


@pytest.fixture(scope='function')
def driver():
    d = BrowserController('edge')
    yield d
    d.close()


@pytest.mark.parametrize(
    "tab,name,description,number,position",
    read_excel_data('test_data.xlsx', 'Sheet2')
)
def test_create_scan_plan(driver, tab, name, description, number, position):
    create_scan_plan(driver, tab, name, description, number, position)

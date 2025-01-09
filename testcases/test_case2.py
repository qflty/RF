import pytest
import allure
from selenium.webdriver.common.by import By
from businesskeys.public import login
from businesskeys.scan import change_directory, switch_tabs, choose_plan, choose_product_type, \
    choose_scan_scope, choose_product, clone_product, delete_product
from position.constants import CREATE_BUTTON, BELONGING_NODE, CHOOSE_NODE, SCAN_TASK_NAME, ADD_BUTTON, SAVE_ONLY_BUTTON
from businesskeys.public import get_number
from testcases.test_login import read_excel_data
from webkeys.webkeys import BrowserController


@allure.title('新建制品扫描任务')
def create_scan_task(driver, tab, plan_name, task_name, type, scope, warehouse, product_name, version, product_path,
                     position=1):
    """
    :param driver:
    :param tab: 制品扫描tab页
    :param plan_name: 方案名称
    :param task_name: 任务名称
    :param type: 制品类型
    :param scope: 扫描范围
    :param warehouse: 制品仓库
    :param product_name: 制品名称
    :param version: 制品版本
    :param product_path: 制品路径
    :param position: 编号位置
    """
    with allure.step('登录devops'):
        login(driver)
    with allure.step('进入制品扫描'):
        change_directory(driver)
    with allure.step('选择tab页'):
        switch_tabs(driver, tab)
    with allure.step('点击创建任务'):
        driver.click(By.XPATH, CREATE_BUTTON)
    with allure.step('选择所属节点'):
        driver.click(By.XPATH, BELONGING_NODE)
        driver.click(By.XPATH, CHOOSE_NODE)
    with allure.step('输入方案名称'):
        choose_plan(driver, plan_name)
    with allure.step('输入任务名称'):
        scan_task_name = task_name + str(get_number(8))
        driver.input(By.XPATH, SCAN_TASK_NAME, scan_task_name)
    with allure.step('选择制品类型'):
        choose_product_type(driver, type)
    with allure.step('选择扫描范围'):
        choose_scan_scope(driver, scope)
    with allure.step('点击添加'):
        driver.click(By.XPATH, ADD_BUTTON)
    with allure.step('选择制品'):
        choose_product(driver, warehouse, product_name, version, product_path, position)
    with allure.step('复制制品'):
        position1 = clone_product(driver, position=1)
    with allure.step('删除制品'):
        delete_product(driver, position1)
    with allure.step('点击保存'):
        driver.click(By.XPATH, SAVE_ONLY_BUTTON)


@pytest.fixture(scope='function')
def driver():
    d = BrowserController('edge')
    yield d
    d.close()


@pytest.mark.parametrize(
    "tab, plan_name, task_name, type, scope, warehouse, product_name, version, product_path, position",
    read_excel_data('test_data.xlsx', 'Sheet3')
)
def test_create_scan_task(driver, tab, plan_name, task_name, type, scope, warehouse, product_name, version, product_path, position):
    create_scan_task(driver, tab, plan_name, task_name, type, scope, warehouse, product_name, version, product_path, position)


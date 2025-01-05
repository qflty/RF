from selenium.webdriver.common.by import By
from businesskeys.public import login, judge_task
from businesskeys.scan import change_directory, switch_tabs, choose_plan, choose_product_type, choose_scan_scope, \
    choose_product, clone_product, delete_product
from position.constants import CREATE_BUTTON, ADD_BUTTON, BELONGING_NODE, CHOOSE_NODE, SCAN_TASK_NAME, SAVE_ONLY_BUTTON
from webkeys.webkeys import BrowserController, get_number


# 创建扫描任务
class CreateScanTask:
    def __init__(self, driver):
        self.driver = driver

    # 登录页面
    def login_succeed(self):
        login(self.driver)

    # 进入制品扫描
    def change_directory_succeed(self):
        change_directory(self.driver)

    # 制品扫描选择tab页
    def switch_tabs_succeed(self, tab):
        switch_tabs(self.driver, tab)

    # 选择方案名称
    def choose_plan_succeed(self, plan_name):
        choose_plan(self.driver, plan_name)

    # 选择制品类型
    def choose_product_type_succeed(self, product_type):
        choose_product_type(self.driver, product_type)

    # 选择扫描范围
    def choose_scan_scope_succeed(self, scope):
        choose_scan_scope(self.driver, scope)

    # 选择制品
    def choose_product_succeed(self, warehouse, product_name, version, product_path, position=1):
        choose_product(self.driver, warehouse, product_name, version, product_path, position)

    # 复制制品
    def clone_product_succeed(self, position):
        result = clone_product(self.driver, position)
        return result

    # 删除制品
    def delete_product_succeed(self, position=1):
        delete_product(self.driver, position)

    def create_task(self, plan_name, task_name, type, scope, warehouse, product_name, version, product_path,
                    position=1):
        """
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
        # 点击扫描方案tab
        self.switch_tabs_succeed('扫描任务')
        # 点击创建按钮
        self.driver.click(By.XPATH, CREATE_BUTTON)
        # 选择所属节点
        self.driver.click(By.XPATH, BELONGING_NODE)
        self.driver.click(By.XPATH, CHOOSE_NODE)
        # 输入方案名称
        self.choose_plan_succeed(plan_name)
        # 输入任务名称
        scan_task_name = task_name + str(get_number(8))
        self.driver.input(By.XPATH, SCAN_TASK_NAME, scan_task_name)
        # 选择制品类型
        self.choose_product_type_succeed(type)
        # 选择扫描范围
        self.choose_scan_scope_succeed(scope)
        # 点击添加
        self.driver.click(By.XPATH, ADD_BUTTON)
        # 选择制品
        self.choose_product_succeed(warehouse, product_name, version, product_path, position)
        # 复制制品
        position1 = self.clone_product_succeed(position=1)
        # 删除制品
        self.delete_product_succeed(position1)
        # 点击保存
        self.driver.click(By.XPATH, SAVE_ONLY_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()
        return scan_task_name


if __name__ == '__main__':
    driver = BrowserController('edge')
    browser_study = CreateScanTask(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    task_name = browser_study.create_task(plan_name="方案验收", task_name="自动化创建", type='Generic',
                                          scope='指定制品扫描', warehouse='demo-generic', product_name='update',
                                          version='11.20', product_path='/')
    sql_template = "select * from neptune_artifact_scan_task where task_name = %s and is_deleted = 'N'"
    judge_task(sql_template, task_name)


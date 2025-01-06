from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from businesskeys.public import login, judge_plan_create
from businesskeys.scan import change_directory, switch_tabs, input_cve_number
from position.constants import CREATE_BUTTON, PLAN_NAME_LOCATER, STE_DEFAULT, PLAN_DESCRIPTION_INPUT, \
    ADD_BUTTON, PLAN_CONFIRM_BUTTON
from webkeys.webkeys import BrowserController, get_number


# 创建扫描方案
class CreateScanPlan:
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

    # 添加漏洞编号
    def input_cve_number_succeed(self, num, txt):
        input_cve_number(self.driver, num, txt)

    def create_plan(self, tab, name, description, number, position=1):
        """
        :param tab: tab页
        :param name: 方案名称
        :param description: 描述
        :param number: 漏洞编号
        :param position: 编号位置
        """
        # 点击扫描方案tab
        self.switch_tabs_succeed(tab)
        # 点击创建按钮
        self.driver.click(By.XPATH, CREATE_BUTTON)
        # 输入方案名称
        scan_plan_name = name + str(get_number(8))
        try:
            self.driver.input(By.XPATH, PLAN_NAME_LOCATER, scan_plan_name)
        except TimeoutException:
            # 处理超时异常，例如记录日志、重试或给出用户提示
            print("无法在指定时间内找到方案名称")
        # 设为默认
        self.driver.click(By.XPATH, STE_DEFAULT)
        # 输入描述
        scan_plan_description = description + str(get_number(8))
        self.driver.input(By.XPATH, PLAN_DESCRIPTION_INPUT, scan_plan_description)
        # 点击添加
        self.driver.click(By.XPATH, ADD_BUTTON)
        # 输入漏洞编号
        self.input_cve_number_succeed(position, number)
        self.driver.click(By.XPATH, PLAN_CONFIRM_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()
        return scan_plan_name


if __name__ == '__main__':
    # 创建 BrowserStudy 类的实例
    driver = BrowserController('edge')
    browser_study = CreateScanPlan(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    plan_name = browser_study.create_plan('扫描方案', "扫描方案E", "自动化创建扫描方案", "CVE-2024-0530")
    judge_plan_create(plan_name)


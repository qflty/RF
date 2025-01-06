from selenium.webdriver.common.by import By
from businesskeys.public import login, judge_plan_delete
from businesskeys.scan import change_directory, switch_tabs, scan_plan_search
from position.constants import DELETE_SCANNER_PLAN, DELETE_CONFIRM_BUTTON, DELETE_CONFIRM
from webkeys.webkeys import BrowserController


# 删除扫描方案
class DeleteScanPlan:
    def __init__(self, driver):
        self.driver = driver

    def login_succeed(self):
        login(self.driver)

    # 进入制品扫描
    def change_directory_succeed(self):
        change_directory(self.driver)

    # 制品扫描选择tab页
    def switch_tabs_succeed(self, tab):
        switch_tabs(self.driver, tab)

    # 扫描方案搜素框
    def scan_plan_search_succeed(self, txt):
        scan_plan_search(self.driver, txt)

    # 删除扫描方案
    def delete_plan(self, tab, plan_name):
        # 点击扫描方案tab
        self.switch_tabs_succeed(tab)
        # 搜索扫描方案
        self.scan_plan_search_succeed(plan_name)
        # 点击删除扫描方案
        self.driver.click(By.XPATH, DELETE_SCANNER_PLAN)
        # 删除弹窗
        self.driver.according_wait(By.XPATH, DELETE_CONFIRM)
        # 弹窗点击确定
        self.driver.click(By.XPATH, DELETE_CONFIRM_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()
        return plan_name


if __name__ == '__main__':
    driver = BrowserController('edge')
    browser_study = DeleteScanPlan(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    plan_name = browser_study.delete_plan('扫描方案', '扫描方案D17259227')
    judge_plan_delete(plan_name)


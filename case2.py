from selenium.webdriver.common.by import By
from businesskeys.public import login, judge_plan_edit
from businesskeys.scan import change_directory, switch_tabs, scan_plan_search
from position.constants import EDIT_SCANNER_PLAN, IMPORT_NUMBER_FILE_lOCATER, VULNERABILITY_NUMBER_FILE, \
    INPORT_NUMBER_BUTTON, IMPORT_NUMBER_CONFIRM_BUTTON, PLAN_CONFIRM_BUTTON
from webkeys.webkeys import BrowserController


# 编辑扫描方案
class EditScanPlan:
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

    # 扫描方案搜索框
    def scan_plan_search_succeed(self, txt):
        scan_plan_search(self.driver, txt)

    # 编辑扫描方案
    def edit_plan(self, plan_name):
        # 点击扫描方案tab
        self.switch_tabs_succeed('扫描方案')
        # 搜索扫描方案
        self.scan_plan_search_succeed(plan_name)
        # 点击编辑扫描方案
        self.driver.click(By.XPATH, EDIT_SCANNER_PLAN)
        # 点击导入编号
        ele = self.driver.locato(By.XPATH, INPORT_NUMBER_BUTTON)
        self.driver.execute_js("arguments[0].click();", ele)
        # 导入漏洞编号文件
        self.driver.input(By.XPATH, IMPORT_NUMBER_FILE_lOCATER, VULNERABILITY_NUMBER_FILE)
        self.driver.click(By.XPATH, IMPORT_NUMBER_CONFIRM_BUTTON)
        self.driver.click(By.XPATH, PLAN_CONFIRM_BUTTON)
        # 截图
        self.driver.sleep(2)
        self.driver.capture()
        # 关闭浏览器
        self.driver.close()
        return plan_name


if __name__ == '__main__':
    driver = BrowserController('edge')
    browser_study = EditScanPlan(driver)
    browser_study.login_succeed()
    browser_study.change_directory_succeed()
    plan_name = browser_study.edit_plan('扫描方案E61663267')  # 输入方案名称
    judge_plan_edit(plan_name, 'CVE-2022-1001')

